def guiexist(windowName):
	#print "{} :not implemented yet".format(sys._getframe().f_code.co_name)
	windowlist = getwindowlist()
	ret = False
	for each in windowlist:
	    if each.endswith(windowName[3:]) != -1:
	        ret = True
	time.sleep(1)
	return ret
	

