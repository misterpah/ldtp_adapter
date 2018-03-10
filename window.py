def guiexist(windowName):
	print "{} :not implemented yet".format(sys._getframe().f_code.co_name)
	windowlist = getwindowlist()
	if windowName in windowlist:
		return True

