ldtp_table = []
ldtp_table.append(["frame","frm"])
ldtp_table.append(["dialog","frm"])
ldtp_table.append(["label","lbl"])
ldtp_table.append(["panel","pnl"])
ldtp_table.append(["text","txt"])
ldtp_table.append(["seperator","seperator"])
ldtp_table.append(["menu item","mnu"])
ldtp_table.append(["list","lst"])
ldtp_table.append(["list item","lstItem"])
ldtp_table.append(["check box","chk"])
ldtp_table.append(["combo box","cbo"])
ldtp_table.append(["unknown","ukn"])
ldtp_table.append(["push button","btn"])
ldtp_table.append(["table","tbl"])
ldtp_table.append(["table cell","tblc"])
ldtp_table.append(["radio button","rbtn"])
ldtp_table.append(["page tab","tab"])
ldtp_table.append(["table column header","tblHeader"])

def reverse_ldtp_me(ldtp_name):
	#print ldtp_name
	name = ldtp_name
	role = "unknown"
	for each in ldtp_table:
		if ldtp_name.startswith(each[1]):
			role = each[0]
			prefix = each[1]
			name = ldtp_name.replace(prefix,"")
	return {"name":name,"role":role}
	

def ldtp_me(name,roleName):
	ret = name
	role = None
	prefix = None
	for each in ldtp_table:
		if roleName == each[0]:
			role = each[0]
			prefix = each[1]
			break
	if role == None:
		prefix = "notImplemented_"+roleName
	if role == "text":
		name = name.replace(":","")
	ret = prefix+name	
	return ret
	"""
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
	"""



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

def search_object_under_mouse(wait_time=0.0,filter=None):
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

	for i,value in enumerate(output):
		output[i]['window'] = windowName
	if filter == None:
		return output
	else:
		for each in output:
			temp = reverse_ldtp_me(each['name'])
			print temp
			for each2 in ldtp_table:
				if temp['role'] == each2[0]:
					if filter == each2[0]:
						return each
					if filter == each2[1]:
						return each
		return []


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
	if final_output != None:
		final_output['window'] = windowName
	return final_output	