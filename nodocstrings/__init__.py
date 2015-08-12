
import logging
import os
import sys
import inspect
from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.nodocstrings')

err = sys.stderr

class NoDocStrings(Plugin):
    name = 'nodocstrings' # invoke with --with-nodocstrings
    enabled = True

    def options(self, parser, env=os.environ):
        super(NoDocStrings, self).options(parser, env=env)

    def configure(self, options, conf):
        super(NoDocStrings, self).configure(options, conf)

    def finalize(self, result):
        pass

    def afterImport(self, filename, module):
        for name, obj in inspect.getmembers(sys.modules[module]):
            if inspect.isfunction(obj) and obj.__name__.startswith('test_'):
                obj.__doc__ = None
