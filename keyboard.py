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
    keys_to_press = regex_keystring(key)
    key_to_press = []
    for each in keys_to_press:
        key_to_press.append(find_key(each))
    # pressing time
    for each in key_to_press:
        
        k.press_key(each)

def keyrelease(key):
    k = PyKeyboard()
    keys_to_press = regex_keystring(key)
    key_to_press = []
    for each in keys_to_press:
        key_to_press.append(find_key(each))
    # pressing time
    for each in key_to_press:
        k.release_key(each)

def _press_key(key_int):
    k = PyKeyboard()
    k.tap_key(key_int)
    time.sleep(0.3)

def regex_keystring(string):
    regex = r"<([A-Za-z]*)>"
    working_string = string
    result = []
    loop = True
    while loop:
        if len(working_string) > 0:
            try:
                found = re.match(regex,working_string)
                result.append(found.group(1))
                start = len(found.group(0))
                working_string = working_string[start:]
            except AttributeError:
                # not found
                result.append(working_string)
                working_string = ""
        else:
            loop = False
    return result

def regex_generatekeyevent(string):
    regex = r"<(.*?)>"
    for each in re.finditer(regex,string):
        string = string.replace(each.group(0),";"+each.group(1)+";")
    return string.split(";")

def generatekeyevent(key):
    k = PyKeyboard()
    key = regex_generatekeyevent(key)
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

