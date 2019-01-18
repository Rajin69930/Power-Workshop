Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> 2+3
5
>>> 2/3
0.6666666666666666
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
Hello World
>>>  print("HELLO WORLD")
SyntaxError: unexpected indent
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
<class 'int'>
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
6.0
>>> name='gg'
>>> print(name)
gg
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
>>> phrase='It\'s a nice day'
>>> 
>>> phrase
"It's a nice day"
>>> "HEllo" + "World"
'HElloWorld'
>>> "Hello"+"World"
'HelloWorld'
>>> "*" * 8
'********'
>>> x="hello"
>>> x[1:4]
'ell'
>>> x[-4:-1]
'ell'
>>> input("Enter Your Name")
Enter Your Name
''
>>> rajin
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    rajin
NameError: name 'rajin' is not defined
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
Enter your full namerajin maharjan
Enter your age19
rajin maharjan
19
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
Enter your full namerajin
Enter your age89
Your name is : ,name
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
Enter your full namerajin
Enter your age8
Your name is :(name)
Your age is : (age)
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
Enter your full namerjain
Enter your age5
Your name is rjain and your age is 5
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
Enter your full namerajin
Enter your age89
Your name is rajin and your age is 89
Your name is rajin and age is 89
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
Enter your full namerajin
Enter your age18
Your name is rajin and your age is 18
Your name is rajin and age is 18
Your name is 18 and age is rajin
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
Traceback (most recent call last):
  File "C:/Users/rajin/Desktop/new.py", line 1, in <module>
    name=r
NameError: name 'r' is not defined
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
Traceback (most recent call last):
  File "C:/Users/rajin/Desktop/new.py", line 1, in <module>
    name=rsad
NameError: name 'rsad' is not defined
>>> 
=================== RESTART: C:/Users/rajin/Desktop/new.py ===================
Your name is r and your age is 12
Your name is r and age is 12
Your name is r and age is 12
Your name is r and age is 12, happy birthday in reaching 12
Your name is r and age is 12
Your name is r and age is 12
>>> Your name is r and age is 12
SyntaxError: invalid syntax
>>> 
>>> import keyword
>>> 
>>> 
================ RESTART: C:/Users/rajin/Desktop/constant.py ================
>>> 
================ RESTART: C:/Users/rajin/Desktop/constant.py ================
Your name is r and your age is 12
Your name is r and age is 12
Your name is r and age is 12
Your name is r and age is 12, happy birthday in reaching 12
Your name is r and age is 12
Your name is r and age is 12
>>> 
================ RESTART: C:/Users/rajin/Desktop/constant.py ================
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
================ RESTART: C:/Users/rajin/Desktop/constant.py ================
Enter agea
Traceback (most recent call last):
  File "C:/Users/rajin/Desktop/constant.py", line 2, in <module>
    int(age)
ValueError: invalid literal for int() with base 10: 'a'
>>> divmod(5.2)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    divmod(5.2)
TypeError: divmod expected 2 arguments, got 1
>>> divmod(5,2)
(2, 1)
>>> x=5
>>> type(x)
<class 'int'>
>>> y="Hello"
>>> type(y)
<class 'str'>
>>> roll_numbers=[1,2,3,4]
>>> type(roll_numbers)
<class 'list'>
>>> coll[1,.2,"HELLO"]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    coll[1,.2,"HELLO"]
NameError: name 'coll' is not defined
>>> p
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    p
NameError: name 'p' is not defined
>>> p=list()
>>> p
[]
>>> p.append(4)
>>> p
[4]
>>> p.append(5)
>>> p
[4, 5]
>>> comp=["00P", "CSA", "NM", "MGMT", "OS"]
>>> comp
['00P', 'CSA', 'NM', 'MGMT', 'OS']
>>> comp.insert(0,"MATH")
>>> comp
['MATH', '00P', 'CSA', 'NM', 'MGMT', 'OS']
>>> del comp[0]
>>> comp
['00P', 'CSA', 'NM', 'MGMT', 'OS']
>>> comp=["00P", "CSA", "NM", "MGMT", "OS"]
>>> comp.extend(comp)
>>> comp
['00P', 'CSA', 'NM', 'MGMT', 'OS', '00P', 'CSA', 'NM', 'MGMT', 'OS']
>>> comp.pop()
'OS'
>>> comp
['00P', 'CSA', 'NM', 'MGMT', 'OS', '00P', 'CSA', 'NM', 'MGMT']
>>> 
