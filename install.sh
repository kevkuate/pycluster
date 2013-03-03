wget https://bitbucket.org/pypy/pypy/downloads/pypy-1.9-linux64.tar.bz2
tar xvf https://bitbucket.org/pypy/pypy/downloads/pypy-1.9-linux64.tar.bz2
rm pypy-1.9-linux64.tar.bz2
mv pypy-1.9 pypy-1.9_64
virtualenv -p pypy-1.9_64/bin/pypy venvlin64
cd venvlin64/bin/
./pypy activate_this.py 
./easy_install jsonpickle Flask simplejson requests

