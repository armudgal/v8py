import pytest

class TestPythonProxy(object):
    @pytest.fixture
    def o(self, context):
        return context.eval('o = {foo: "bar"}')

    def test_keys(self, o):
        assert o.keys() == ['foo']

    def test_length(self, o):
        assert len(o) == 1

    def test_getitem(self, o):
        assert o['foo'] == 'bar'

    def test_setitem(self, o):
        o['foo'] = 'baz'
        assert o['foo'] == 'baz'

    def test_delitem(self, o):
        del o['foo']
        assert len(o) == 0
        assert dict(o) == {}

    def test_in(self, o):
        assert 'foo' in o
        assert 'bar' not in o

    def test_repr(self, o):
        assert repr(o) == repr(dict(o))
        assert str(o) == str(dict(o))

    def test_dictification(self, o):
        assert dict(o) == {'foo': 'bar'}

    def test_listification(self, o):
        assert list(o) == ['foo']

    @pytest.mark.xfail
    def test_unconfigurable(self, context):
        context.eval('o = ({})')
        context.eval('Object.defineProperty(o, "foo", {value: "bar", configurable: false})')
        with pytest.raises(TypeError):
            del context.o['foo']


