def selectmenuitem(window,object):
    log("{} :not implemented yet".format(sys._getframe().f_code.co_name))
    object = object.split(";")
    debug(window,object)
    debug(pyacc.getObject(window,object[0]))
    if len(object) == 2:
        mousemove(window,object[0])
        ldtp_extend_mouse_click_here()
        time.sleep(1)
        objectHandle = pyacc.getObject(window,object[1])
        try:
            objectHandle[0]
            #debug(objectHandle[1]['return'])
            mousemove(window,object[1],handle=objectHandle[1]['return']['handle'])
            ldtp_extend_mouse_click_here()
        except IndexError:
            return False

