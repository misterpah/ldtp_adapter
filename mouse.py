def mousemove(window,object):
	pyacc.mouseMove(window,object)
		
def click(window,object):
	pyacc.mouseClick(window,object)
			
def ldtp_extend_mouse_click_here():
	m = PyMouse()
	pos = m.position()
	m.click(pos[0],pos[1],1)
	
def ldtp_extend_mouse_right_click_here():
	m = PyMouse()
	pos = m.position()
	m.click(pos[0],pos[1],2)
