# IPython log file

import os
import requests_cache
import requests
requests


DEFAULT_FILENAME = 'cache.sqlite'

def delete_cache(filename=DEFAULT_FILENAME):
    os.path.isfile(filename) and os.remove(filename)

def install_cache(filename=DEFAULT_FILENAME):
    #requests_cache.install_cache()
    requests_cache.install_cache(
            #location='data/redem',
            backend='sqlite',
            expire_after=60*60,
            fast_save=True)


def do_regular_requests_stuffs():
    resp = requests.get('http://google.com')
    return resp

def assert_requests_cache(filename=DEFAULT_FILENAME):
    import IPython
    #ipy = get_ipython()
    ipy = IPython.core.ipapi.get()
    print(ipy.getoutput(u'ls'))
    print(ipy.getoutput(u'sqlite3 %r .dump' % filename) )


def do_reddit_stuffs():
    import praw
    reddit = praw.Reddit(user_agent="Test/0.0.1")
    reddit.get_redditor('westurner')

delete_cache()

install_cache()
assert_requests_cache()

do_reddit_stuffs()
assert_requests_cache()

do_reddit_stuffs()
assert_requests_cache()

