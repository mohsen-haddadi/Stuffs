import time, tkinter
"""
if 'pip install win32api' lead to error,
'pip install pywinutils' instead,
and then simply 'import win32api'
"""
import pyautogui, win32api

try:
    import pygetwindow
except Exception as e:
    print(e)


print("Press 'Enter' to get pixel color")

window = tkinter.Tk()

window.title("pixel color")
window.geometry('230x80')

#https://www.quora.com/How-do-I-detect-mouse-events-left-click-with-Python
# Left button down = 0 or 1. Button up = -127 or -128 
#state_left = win32api.GetKeyState(0x01)
# 'enter' key: 
state_left = win32api.GetKeyState(13) 

count = 0
while True: 
    #a = win32api.GetKeyState(0x01) 
    a = win32api.GetKeyState(13)

    if a != state_left:  # Button state changed 

        state_left = a 
        if a < 0:
            x, y = pyautogui.position()
            pixel_color = pyautogui.pixel(x, y)
            count += 1
            print('pixel number %s: %s'%(count, pixel_color))
            
            rgb = tkinter.Text(window, background='#%02x%02x%02x' % pixel_color)
            rgb.tag_configure('big', font=('Arial', 20))
            rgb.insert(tkinter.END, "(%s, %s, %s)"%pixel_color, 'big')
            rgb.grid(column=0, row=0)
            window.update()

            try:
                win = pygetwindow.getWindowsWithTitle('pixel color')[0]
                win.restore()
                win.activate()
            except Exception as e:
                if count == 1:
                    print(e)


    window.update()
    time.sleep(0.001)