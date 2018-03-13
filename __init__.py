import os,sys,time
import pyaccessibility as pyacc
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from difflib import SequenceMatcher

ldtp_pyaccessibility_path = os.path.dirname(os.path.abspath(__file__))
files_in_folders = os.listdir(ldtp_pyaccessibility_path)
for each in files_in_folders:
	if each.endswith(".py"):
		if each.startswith("__init__") is False:
			execfile(os.path.join(ldtp_pyaccessibility_path, each))
