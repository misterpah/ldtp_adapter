def ldtp_me(name,roleName):
	ret = name
	if roleName == "frame":
		ret = "frm"+name
	elif roleName == "dialog":
		ret = "frm"+name
	elif roleName == "label":
		ret = "lbl"+name	
	elif roleName == "panel":
		ret = "pnl"+name			
	elif roleName == "text":
		name = name.replace(":","")
		ret = "txt"+name	
	elif roleName == "separator":
		ret = "seperator"+name			
	elif roleName == "menu item":
		ret = "mnu"+name		
	elif roleName == "list":
		ret = "lst"+name
	elif roleName == "list item":
		ret = "lstItem"+name
	elif roleName == "check box":
		ret = "chk"+name
	elif roleName == "combo box":
		ret = "cbo"+name		
	elif roleName == "unknown":
		ret = "ukn"+name				
	elif roleName == "push button":
		ret = "btn"+name
	elif roleName == "table":
		ret = "tbl"+name
	elif roleName == "table cell":
		ret = "tblc"+name		
	elif roleName == "radio button":
		ret = "rbtn"+name				
	elif roleName == "page tab":
		ret = "tab"+name		
	elif roleName == "table column header":
		ret = "tblHeader"+name		
	else:
		ret = "notImplemented_"+roleName+name
	return ret


def getwindowlist():
	ret = []
	for each in pyacc.getWindowList():
		ret.append(ldtp_me(each['name'],each['role']))
	return ret

def getobjectproperty(window,object,property):
	print "{} :not Fully implemented yet".format(sys._getframe().f_code.co_name)
	ret = None
	if property == "label":
		objHandle = getobjecthandle(window,object)
		ret = objHandle.get('name')
	return ret

def getobjecthandle(window,objectName):
	ret = None
	similar_index = 0
	for each in pyacc.getObjectList(window):
	    ldtp_name = ldtp_me(each[0]['name'],each[0]['role'])
	    if ldtp_name == objectName:
	        ret = each[0]

	if ret == None:
	    for each in pyacc.getObjectList(window):
			ldtp_name = ldtp_me(each[0]['name'],each[0]['role'])
			if similar(objectName,ldtp_name) > similar_index:
				similar_index = similar(objectName,ldtp_name)
				ret = each[0]
	return ret

       
def getobjectlist(window):
	ret = []
	for each in pyacc.getObjectList(window):
		ret.append(ldtp_me(each[0]['name'],each[0]['role']))
	return ret	

def similar(a, b):
    return jellyfish.jaro_distance(unicode(a,"utf-8"),unicode(b,"utf-8"))

def getobjectnameatcoords(wait_time=0.0):
	time.sleep(wait_time)
	ret = []
	output = _getobjectnameatcoords()
	ret.append(output['window'])
	ret.append(output['name'])
	return ret

def _getobjectnameatcoords():
	#get active window
	active_window = pyacc.getActiveWindow()['name']
	highest = 0
	cur_highest = None
	for each in getwindowlist():
		if similar(each,active_window) > highest:
			highest = similar(each,active_window)
			cur_highest = each
	windowName = cur_highest

	m = PyMouse()
	pos = m.position()
	
	# checking if mouse can detect object at mouse position
	output = []
	for each in pyacc.getObjectList(windowName):
		handle = each[0]['handle']
		name = ldtp_me(each[0]['name'],each[0]['role'])
		rect = pyacc.getObjectRect(handle)
		if pos[0] > rect['x'][0]:
			if pos[0] <= rect['x'][1]:
				if pos[1] > rect['y'][0]:
					if pos[1] <= rect['y'][1]:
						output.append({"handle":handle,"name":name,"rect":rect})
	
	final_output = None
	for each in output:
		if each['handle'].getChildCount() == 0:
			final_output = each
	final_output['window'] = windowName
	return final_output
	"""
	for each in getobjectlist(windowName):
	    size = handle.queryComponent().getSize()
	    pos = handle.queryComponent().getPosition(pyatspi.DESKTOP_COORDS)
	"""
	