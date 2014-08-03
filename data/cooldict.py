#!/usr/bin/env python
# encoding: utf-8
from __future__ import print_function
"""
cooldict
"""

SENTINEL='AWESOME'

from collections import OrderedDict


def get_default(self, key, value=SENTINEL):
    if value == SENTINEL:
        default_value = dict()
    else:
        default_value = value
    return self.get(key, default_value)


class AwesomeDict(OrderedDict):
    Get = get_default


from collections import defaultdict
class AwesomeDefaultDict(defaultdict):
    Get = get_default


def cooldict():
    """
    mainfunc
    """
    # data.get('_meta',{}).get('username')

    print( _do_this(None, AwesomeDict) )


def _do_this(self, cls):
    d = cls()
    d['one'] = 1
    d['two'] = 2
    d['three'] = cls(three_one="3.1")
    print(d)
    print(d.Get('one'))
    print(d.Get('three').Get('three_one', None))


import unittest
class Test_cooldict(unittest.TestCase):
    do_this = _do_this

    def test_awesomedict(self):
        self.do_this(AwesomeDict)

    def test_awesomedefaultdict(self):
        self.do_this(AwesomeDefaultDict)


def main():
    import optparse
    import logging

    prs = optparse.OptionParser(usage="./%prog : args")

    prs.add_option('-v', '--verbose',
                    dest='verbose',
                    action='store_true',)
    prs.add_option('-q', '--quiet',
                    dest='quiet',
                    action='store_true',)
    prs.add_option('-t', '--test',
                    dest='run_tests',
                    action='store_true',)

    (opts, args) = prs.parse_args()

    if not opts.quiet:
        logging.basicConfig()

        if opts.verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    if opts.run_tests:
        import sys
        sys.argv = [sys.argv[0]] + args
        import unittest
        exit(unittest.main())

    cooldict()

if __name__ == "__main__":
    main()


