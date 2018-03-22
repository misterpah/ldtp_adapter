def selectmenuitem(window,object):
    #log("{} :not implemented yet".format(sys._getframe().f_code.co_name))
    object = object.split(";")
    if len(object) == 2:
        objectHandle = getobjecthandle(window,object[0])['handle']
        mousemove(window,object[0],handle=objectHandle)
        ldtp_extend_mouse_click_here()
        time.sleep(1)
        objectHandle = getobjecthandle(window,object[1])['handle']
        mousemove(window,object[1],handle=objectHandle)
        ldtp_extend_mouse_click_here()
