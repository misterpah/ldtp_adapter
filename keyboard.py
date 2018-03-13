import re
def _find_key(keyString):
    k = PyKeyboard()
    key_to_press = None
    highest = 0
    if keyString.startswith("<"):
        cur_key = keyString[1:-1]
        for each in dir(k):
            if each.endswith("_key"):
                if similar(cur_key + "_key" ,each) > highest:
                    highest = similar(cur_key + "_key" ,each)
                    key_to_press = getattr(k,each)
    else:
        key_to_press = keyString
        #key_to_press = k.lookup_character_keycode(keyString)
        #if keyString == "_":
        #    key_to_press = [k.shift_key,k.lookup_character_keycode(keyString)]
            
        
    return key_to_press
    
def keypress(key):
    k = PyKeyboard()
    key_to_press = _find_key(key)
    if key_to_press != None:
        k.press_key(key_to_press)

def keyrelease(key):

    k = PyKeyboard()
    key_to_press = _find_key(key)
    if key_to_press != None:
        k.release_key(key_to_press)

def _press_key(key):
    keypress(key)
    keyrelease(key)
    time.sleep(0.3)

def generatekeyevent(key):
    #print "{} :not implemented yet".format(sys._getframe().f_code.co_name)
    key_to_press =[]
    if key.startswith("<"):
        regex = r"(<.[^(><.)]+>)"
        key = re.findall(regex,key)
    for each in key:
        key_to_press.append(_find_key(each))
    try:
        for each in key_to_press:
            _press_key(each)
    except TypeError:
        _press_key(key_to_press)

