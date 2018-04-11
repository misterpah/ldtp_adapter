def selectitem(windowTitle, object, value, handle=None):
    log("{} :not implemented yet".format(sys._getframe().f_code.co_name))
    options = pyacc.comboboxListOptions(reverse_ldtp_me(windowTitle),reverse_ldtp_me(object),handle)
    # get position of the wanted item
    for each in range(0,len(options)):
        if options[each] == value:
            break
    # get position of the selected item
    selected = pyacc.comboboxGetSelected(reverse_ldtp_me(windowTitle),reverse_ldtp_me(object),handle)
    selected_index = options.index(selected)
    # calculate how many keypress needed
    diff = each - selected_index
    key = ""
    if diff == 0:
        # no need to move anything
        return 1
    elif diff > 0:
        #positive. move down
        key = "<down>"
    else:
        #negative. move up
        key = "<up>"
        diff *= -1
    # apply changes
    ldtp_extend_mouse_click_here()
    for each in range(0,diff):
        keypress(key)
        keyrelease(key)
        time.sleep(0.1)
    keypress("<enter>")
    keyrelease("<enter>")