def mousemove(window,object,handle=None):
	debug("mousemove",window,object)
	window = reverse_ldtp_me(window)
	object = reverse_ldtp_me(object)
	pyacc.mouseMove(window,object,handle)
	time.sleep(MOUSEDELAY)

def mouseleftclick(window,object):
    #debug(window,object)
    click(window,object)
    time.sleep(MOUSEDELAY)
    return 1

def click(window,object):
	#debug("click",window,object)
	window = reverse_ldtp_me(window)
	object = reverse_ldtp_me(object)
	#print window , object	
	pyacc.mouseClick(window,object)
	time.sleep(MOUSEDELAY)
			
def ldtp_extend_mouse_click_here():
	m = PyMouse()
	pos = m.position()
	m.click(pos[0],pos[1],1)
	time.sleep(MOUSEDELAY)
	
def ldtp_extend_mouse_right_click_here():
	m = PyMouse()
	pos = m.position()
	m.click(pos[0],pos[1],2)
	time.sleep(MOUSEDELAY)

