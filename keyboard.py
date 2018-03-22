import re
def find_key(keyString):
    k = PyKeyboard()
    key_to_press = None
    highest = 0
    for each in dir(k):
        if each.endswith("_key"):
            if similar(keyString + "_key" ,each) > highest:
                highest = similar(keyString + "_key" ,each)
                key_to_press = getattr(k,each)
    return key_to_press
    
def keypress(key):
    k = PyKeyboard()
    key_to_press = find_key(key)
    #print key_to_press
    if key_to_press != None:
        try:
            k.press_key(key_to_press)
        except TypeError:
            for each in key_to_press:
                k.press_key(each)

def keyrelease(key):
    k = PyKeyboard()
    key_to_press = find_key(key)
    if key_to_press != None:
        try:
            k.release_key(key_to_press)
        except TypeError:
            for each in key_to_press:
                k.release_key(each)        

def _press_key(key_int):
    k = PyKeyboard()
    k.tap_key(key_int)
    time.sleep(0.3)

def regex_keystring(string):
    regex = r"<(.*?)>"
    for each in re.finditer(regex,string):
        string = string.replace(each.group(0),";"+each.group(1)+";")
    return string.split(";")

def generatekeyevent(key):
    k = PyKeyboard()
    key = regex_keystring(key)
    if len(key) == 1:
        for cur in key[0]:
            k.tap_key(cur)
            time.sleep(0.3)
    else:
        for each in key:
            if each == "":
                continue
            cur_key = find_key(each)
            if cur_key == None:
                for cur in each:
                    k.tap_key(cur)
                    time.sleep(0.3)
            else:
                k.tap_key(cur_key)
                time.sleep(0.3)

