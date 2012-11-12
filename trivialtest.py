import socket
from struct import *
import Queue
import socket
import pickle
import time
import sqlite3
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import hashlib
import sys
from email.parser import Parser
from time import strftime, localtime
import cStringIO
import sqlite3



APPNAME = "trivialtest"
from os import path, environ
if sys.platform == 'darwin':
    from AppKit import NSSearchPathForDirectoriesInDomains
    # http://developer.apple.com/DOCUMENTATION/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Functions/Reference/reference.html#//apple_ref/c/func/NSSearchPathForDirectoriesInDomains
    # NSApplicationSupportDirectory = 14
    # NSUserDomainMask = 1
    # True for expanding the tilde into a fully qualified path
    appdata = path.join(NSSearchPathForDirectoriesInDomains(14, 1, True)[0], APPNAME) + '/'
elif sys.platform == 'win32':
    appdata = path.join(environ['APPDATA'], APPNAME) + '\\'
else:
    appdata = path.expanduser(path.join("~", "." + APPNAME + "/"))

print appdata