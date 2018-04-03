def mousemove(window,object,handle=None):
	debug("mousemove",window,object)
	pyacc.mouseMove(window,object,handle)
	time.sleep(MOUSEDELAY)

def mouseleftclick(window,object):
    debug(window,object)
    click(window,object)
    log("{} :not implemented yet".format(sys._getframe().f_code.co_name))
    time.sleep(MOUSEDELAY)

def click(window,object):
	debug("click",window,object)
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

