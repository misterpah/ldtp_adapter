def gettextvalue(window,object):
    print "{} :not implemented yet".format(sys._getframe().f_code.co_name)
    window = reverse_ldtp_me(window)
    object = reverse_ldtp_me(object)
    result = pyacc.getObject(window,object)
    ret = None
    if result['handle']:
        textObj = result['handle'].queryText()
        ret = textObj.getText(0,textObj.characterCount)
    return ret
    
def settextvalue(window,object,text):
    print "{} :not implemented yet".format(sys._getframe().f_code.co_name)
    click(window,object)
    generatekeyevent(text)

