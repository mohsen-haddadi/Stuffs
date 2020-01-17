Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\office\Desktop\DESKTOP\Python poker\ALL SCRIPTS\New-FUNCTIONS.py 
>>> 
 RESTART: C:\Users\office\Desktop\DESKTOP\Python poker\ALL SCRIPTS\New-FUNCTIONS.py 
>>> Card_1th="2 c"; Card_2th="4 c"; Card_3th="7 c"; Card_4th="5 c"; Card_5th="8 h"
>>> Turn_str_2_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th )
[(6, 3), (1, 3), (6, 8), (3, 6), (8, 6), (3, 1)]
>>> Flop_str_2_Cards_list( Card_1th, Card_2th, Card_3th )
[]
>>> Card_1th="2 c"; Card_2th="3 c"; Card_3th="5 c"; Card_4th="6 c"; Card_5th="8 h"
>>> Flop_str_2_Cards_list( Card_1th, Card_2th, Card_3th )
[(1, 4), (4, 1), (4, 6), (6, 4)]
>>> a=[]
>>> for b in a:
	print(b)

	
>>> a=[(1, 4), (4, 1), (4, 6), (6, 4)]
>>> z=[]
>>> for b in z:
	print(2)

	
>>> max(a[0])
4
>>> min(a[0])
1
>>> z=[(4, 4)]
>>> max(z[0])
4
>>> min(z[0])
4
>>> z.remove(2)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    z.remove(2)
ValueError: list.remove(x): x not in list
>>> 
 RESTART: C:\Users\office\Desktop\DESKTOP\Python poker\ALL SCRIPTS\New-FUNCTIONS.py 
>>> Card_1th="2 c"; Card_2th="3 c"; Card_3th="5 c"; Card_4th="6 c"; Card_5th="8 h"
>>> Flop_str_2_Cards_list( Card_1th, Card_2th, Card_3th )
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Flop_str_2_Cards_list( Card_1th, Card_2th, Card_3th )
  File "C:\Users\office\Desktop\DESKTOP\Python poker\ALL SCRIPTS\New-FUNCTIONS.py", line 82, in Flop_str_2_Cards_list
    Flop_str_2_Cards_list.remove(min(tuples),max(tuples))
TypeError: remove() takes exactly one argument (2 given)
>>> 
 RESTART: C:\Users\office\Desktop\DESKTOP\Python poker\ALL SCRIPTS\New-FUNCTIONS.py 
>>> Card_1th="2 c"; Card_2th="3 c"; Card_3th="5 c"; Card_4th="6 c"; Card_5th="8 h"
>>> Flop_str_2_Cards_list( Card_1th, Card_2th, Card_3th )
[(6, 4), (4, 1)]
>>> 
 RESTART: C:\Users\office\Desktop\DESKTOP\Python poker\ALL SCRIPTS\New-FUNCTIONS.py 
>>> Card_1th="2 c"; Card_2th="3 c"; Card_3th="5 c"; Card_4th="6 c"; Card_5th="8 h"
>>> Flop_str_2_Cards_list( Card_1th, Card_2th, Card_3th )
[(6, 4), (4, 1)]
>>> Turn_str_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th )
[4]
>>> Turn_str_2_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th )
[(7, 4)]
>>> River_str( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th )
>>> River_str_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th )
[]
>>> River_str_2_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th, Card_5th )
[(9, 7)]
>>> Flop_open_str_draw_1_Cards_list( Card_1th, Card_2th, Card_3th )
[4]
>>> Flop_open_str_draw_2_Cards_list( Card_1th, Card_2th, Card_3th )
[]
>>> Turn_open_str_draw_1_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th )
[]
>>> Turn_open_str_draw_2_Cards_list( Card_1th, Card_2th, Card_3th, Card_4th )
[(9, 8), (8, 7)]
>>> 



            if str_length( Loop_List ) == 6 and min(Loop_List) not in (i,j)\
            and str_length( list( set([Card_1th, Card_2th, Card_3th, Card_4th, Card_5th]) | set([i]) ) ) !=6 \
            and str_length( list( set([Card_1th, Card_2th, Card_3th, Card_4th, Card_5th]) | set([j]) ) ) !=6 :
                River_str_2_Cards_list.append((i,j))
