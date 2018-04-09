import os,sys,time
import pyaccessibility as pyacc
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from difflib import SequenceMatcher
import jellyfish
import pyatspi #for checking constants

MOUSEDELAY=0.5
DEBUG = True

if DEBUG:
    import code

def log(*string):
    print string

def debug(*string):
    if DEBUG:
        print string

def interactive():
    code.interact(local=locals())


ldtp_pyaccessibility_path = os.path.dirname(os.path.abspath(__file__))
files_in_folders = os.listdir(ldtp_pyaccessibility_path)
for each in files_in_folders:
	if each.endswith(".py"):
		if each.startswith("__init__") is False:
			execfile(os.path.join(ldtp_pyaccessibility_path, each))
