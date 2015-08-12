# nosenodocstrings
A small plugin that prevents nosetests from display docstrings instead of function names in verbosity mode (-v)

## Install

```bash
python setup.py install
```

Works with python3 and python2

## Usage

```bash
nosetests -v --with-nodocstrings
```

## Notes

Will work only with function.
It should be easy enough to add methods as well.

Enjoy.