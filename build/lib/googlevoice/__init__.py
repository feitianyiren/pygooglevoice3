"""
This project aims to bring the power of the Google Voice API to the Python language in a simple,
easy-to-use manner. Currently it allows you to place calls, send sms,
download voicemails/recorded messages, and search the various folders of your Google Voice Accounts.
You can use the Python API or command line script to schedule calls, check for new received calls/sms,
or even sync your recorded voicemails/calls.
Works for Python 2.

----------------------

This version has been updated by David Stewart to work with Python 3

"""
__author__ = 'David Stewart'
__email__ = 'dstewart@cct.lsu.edu',
__copyright__ = 'Copyright 2009, Justin Quick and Joe McCall'
__credits__ = ['Justin Quick','Joe McCall','Jacob Feisley','John Nagle']
__license__ = 'New BSD'
__version__ = '1.0'

from .voice import Voice
from .util import Phone, Message, Folder