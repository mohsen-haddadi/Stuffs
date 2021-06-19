import pygetwindow

def chrome(table):
    win = pygetwindow.getWindowsWithTitle('Chrome')[0]
    if table == 1:
        win.size = (974, 1047)
        win.moveTo(-7, 0)
    elif table == 2:
        win.size = (974, 1047)
        win.moveTo(953, 0)
    elif table == 'test':
        win.size = (974, 2047)
        win.moveTo(-7, 0)
    #print(win.size)
    #print(win.topleft)

chrome(1)