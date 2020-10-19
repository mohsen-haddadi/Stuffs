#OK
import os, re
from datetime import datetime

from painter import paint

import config

paint.enabled = True # for cmd use

def shout(string, color = None, save = True) :
    """Set save to False if you want to test this module independently."""
    #global DATED_REPORT_FOLDER

    if color == None:
        pass 
    elif color == 'light_cyan':
        string = paint.light_cyan.bold(string)
    elif color == 'green':
        string = paint.green.bold(string)
    elif color == 'light_green':
        string = paint.light_green.bold(string)
    elif color == 'yellow':
        string = paint.yellow.bold(string)
    elif color == 'light_magenta':
        string = paint.light_magenta.bold(string)

    elif color == 'rainbow':
        string = paint.rainbow.bold(string)

    elif color == 'on_green':
        string = paint.on_green.bold(string)
    elif color == 'on_light_blue':
        string = paint.on_light_blue.bold(string)
    elif color == 'on_yellow':
        string = paint.on_yellow.bold(string)
    elif color == 'on_light_magenta':
        string = paint.on_light_magenta.bold(string)
    elif color == 'on_light_red':
        string = paint.on_light_red.bold(string)


    date_and_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
    date_and_time = date_and_time[:-4]

    if 'PROMPT' in os.environ :
        try:
            print("%s: %s" %(date_and_time, string))
        except:
            # To refuse print error on cmd, this line will convert '”f5,628K'
            # to 'f5,628K'. But on .txt file in report folder the string is 
            # saved '”f5,628K' unchanged.
            ascii_string = string.encode('utf-8').decode('ascii', 'ignore')
            #ascii_string = str(ascii_string)
            print("%s: %s" %(date_and_time, ascii_string))
        # Clear the paint effects on string to make string raw and readable
        string = re.sub(r'\x1b(\[.*?[@-~]|\].*?(\x07|\x1b\\))', '', string)
    else :
        # Clear the paint effects on string to make string raw and readable
        string = re.sub(r'\x1b(\[.*?[@-~]|\].*?(\x07|\x1b\\))', '', string)
        print("%s: %s" %(date_and_time, string))

    if save:
        text_file_name = os.path.join("Reports/%s" %config.DATED_REPORT_FOLDER,
                                      config.DATED_REPORT_FOLDER)
        text_file = open("%s.txt" %text_file_name , "a")
        try:
            text_file.write("%s: %s" %(date_and_time, string))
        except:
            ascii_string = string.encode('utf-8').decode('ascii', 'ignore')
            text_file.write("%s: %s" %(date_and_time, ascii_string))
        text_file.write( "\n" )
        text_file.close()
# Test colors in Command Prompt:
#shout('light_cyan', 'light_cyan', save = False) ; shout('green', 'green', save = False)
#shout('light_green', 'light_green', save = False); shout('yellow', 'yellow', save = False) 
#shout('light_magenta', 'light_magenta', save = False); shout('rainbow', 'rainbow', save = False)
#shout('on_green', 'on_green', save = False); shout('on_light_blue', 'on_light_blue', save = False)
#shout('on_yellow', 'on_yellow', save = False) 
#shout('on_light_magenta', 'on_light_magenta', save = False)
#shout('on_light_red', 'on_light_red', save = False)
