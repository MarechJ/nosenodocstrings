# nosenodocstrings
A small plugin that prevents nosetests from displaying docstrings instead of function names in verbosity mode (-v)

## Install

```bash
python setup.py install
```

```bash
python3 setup.py install
```

Works with python3 and python2

## Usage

```bash
nosetests -v --with-nodocstrings
```

```bash
nosetests3 -v --with-nodocstrings
```

## Notes

It will work only with functions.
It should be easy enough to make it work with classes and methods as well.

The code is kind of a 'workaround', but it does the work for now.

Enjoy.