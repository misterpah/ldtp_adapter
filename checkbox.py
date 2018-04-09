def verifycheck(window,object):
	handle = getobjecthandle(window,object)
	result = False
	if pyacc.checkObjectState(handle['handle'],pyatspi.STATE_CHECKED) == True:
		result = True
	return result
def verifyuncheck(window,object):
	handle = getobjecthandle(window,object)
	result = False
	if pyacc.checkObjectState(handle['handle'],pyatspi.STATE_CHECKED) == False:
		result = True
	return result
def uncheck(window,object):
	handle = getobjecthandle(window,object)
	if pyacc.checkObjectState(handle['handle'],pyatspi.STATE_CHECKED) == False:
		pass
	else:
		mousemove(window,object)
		ldtp_extend_mouse_click_here()
	
def check(window,object):
	handle = getobjecthandle(window,object)
	if pyacc.checkObjectState(handle['handle'],pyatspi.STATE_CHECKED) == True:
		pass
	else:
		mousemove(window,object)
		ldtp_extend_mouse_click_here()

	
