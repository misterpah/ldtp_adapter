def guiexist(windowName):
	#print "{} :not implemented yet".format(sys._getframe().f_code.co_name)
	windowlist = getwindowlist()
	debug(windowlist,windowName)
	ret = False
	for each in windowlist:
	    if each.endswith(windowName[3:]) != -1:
	        ret = True
	time.sleep(1)
	return ret
	
def find_child_window(window):
    print "{} :not implemented yet".format(sys._getframe().f_code.co_name)
