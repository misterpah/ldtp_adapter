def checkrow(window,object):
    log("{} :not implemented yet".format(sys._getframe().f_code.co_name))
    handle = getobjecthandle(window,object)
    if pyacc.checkObjectState(handle['handle'],pyatspi.STATE_CHECKED) == False:
        click(window,object)
    else:
        mousemove(window,object)
    return pyacc.checkObjectState(handle['handle'],pyatspi.STATE_CHECKED)

def uncheckrow(window,object):
    log("{} :not implemented yet".format(sys._getframe().f_code.co_name))
    handle = getobjecthandle(window,object)
    if pyacc.checkObjectState(handle['handle'],pyatspi.STATE_CHECKED) == True:
        click(window,object)
    else:
        mousemove(window,object)
    ret = True
    result = pyacc.checkObjectState(handle['handle'],pyatspi.STATE_CHECKED)
    if result == True:
        ret = False
    return ret
