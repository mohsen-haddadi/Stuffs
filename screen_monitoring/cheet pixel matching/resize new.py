import pygetwindow

def chrome():
    win = pygetwindow.getWindowsWithTitle('Chrome')[0]
    win.size = (1366+12, 768-34)
    win.moveTo(-6, 0)