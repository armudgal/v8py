#!/bin/bash
set -e -x

# Install a system package required by our library
#yum install -y atlas-devel
export PATH=/opt/python/cp27-cp27m/bin:$PATH
python2.7 -V

# Compile wheels
for PYBIN in /opt/python/*/bin; do
    "${PYBIN}/pip" wheel /io/ -w wheelhouse/
done

# Bundle external shared libraries into the wheels
for whl in wheelhouse/*.whl; do
    auditwheel repair "$whl" -w /io/wheelhouse/
done

# Install packages and test
for PYBIN in /opt/python/*/bin/; do
    "${PYBIN}/pip" install v8py --no-index -f /io/wheelhouse
done
