Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3]
>>> l*5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> x=(1,2,3)
>>> x{0}
SyntaxError: invalid syntax
>>> x[0]
1
>>> a=("1")
>>> a
'1'
>>> a=(1)
>>> a
1
>>> type(a)
<class 'int'>
>>> a=(1,)
>>> type(a)
<class 'tuple'>
>>> tup = (1, 2, 3)
print(tup)
tup = tup + (4,)
print(tup)
SyntaxError: multiple statements found while compiling a single statement
>>> tup = (1, 2, 3)
>>> print(tup)
(1, 2, 3)
>>> tup=tup+(4,)
>>> print(tup)
(1, 2, 3, 4)
>>> x=1,2,3
>>> x
(1, 2, 3)
>>> p,q,r =x
>>> p
1
>>> q
2
>>> r
3
>>> name,age,_class=("Ram",45,12)
>>> name
'Ram'
>>> age
45
>>> _class
12
>>> a=4
>>> n=s
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    n=s
NameError: name 's' is not defined
>>> a=4
>>> b=5
>>> a,b=b,a
>>> a
5
>>> b
4
>>> s={"Hello",1,1.5,("OK",None)}
>>> s.update(("Hellooo",2))
>>> print(s)
{1, 1.5, 2, 'Hellooo', ('OK', None), 'Hello'}
>>> str1="Hello my name is ram"
>>> str2="Ram is my name"
>>> str1_set=set(str1.split(" "))
>>> str2_set=set(str2.split(" "))
>>> print(str1_set.intersection(str2_set))
{'my', 'name', 'is'}
>>> d={
	"a":47,
	"b":55,
	"c":89
	}
>>> d.key()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'
>>> d
{'a': 47, 'b': 55, 'c': 89}
>>> d['y']=800
>>> d
{'a': 47, 'b': 55, 'c': 89, 'y': 800}
>>> lem(d)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    lem(d)
NameError: name 'lem' is not defined
>>> len(d)
4
>>> x={1:3}
>>> d.update(x)
>>> d
{'a': 47, 'b': 55, 'c': 89, 'y': 800, 1: 3}
>>> hash(d)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    hash(d)
TypeError: unhashable type: 'dict'
>>> hash("a")
723031980
>>> hash("a")
723031980
>>> d={
	"name":"Rajin",
	"subjects":["python","JS","Java"]
	}
>>> l=list(range(0,10))
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for l==1,3,5,7,9
SyntaxError: invalid syntax
>>> for l=1,3,5,7,9
SyntaxError: invalid syntax
>>> 
=============== RESTART: C:/Users/rajin/Desktop/jan 19/even.py ===============
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
=============== RESTART: C:/Users/rajin/Desktop/jan 19/even.py ===============
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
=============== RESTART: C:/Users/rajin/Desktop/jan 19/even.py ===============
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 2, 4, 6, 8]
>>> a,b=5,8
>>> if a>b:
	print(a)
	else:
		
SyntaxError: invalid syntax
>>> if a>b:
	print(a)
	else:
		
SyntaxError: invalid syntax
>>> if a>b:
	print(a)
    else:print(b)
    
SyntaxError: unindent does not match any outer indentation level
>>> if a>b:
	print(a)
    else:print(b)
    
SyntaxError: unindent does not match any outer indentation level
>>> if a>b:
	print(a)
    else
    
SyntaxError: unindent does not match any outer indentation level
>>> def function_name
SyntaxError: invalid syntax
>>> def function_name
SyntaxError: invalid syntax
>>> def function_name:
	
SyntaxError: invalid syntax
>>> def sum(a,b):
	print(a+b)

	
>>> sum(2,3)
5
>>> def add(a,b):
	print(a+b)

	
>>> add(2.5)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    add(2.5)
TypeError: add() missing 1 required positional argument: 'b'
>>> add(2,5)
7
>>> def sum(a,b):
	return a+b

>>> sum(2,3)
5
>>> res=sum(2,3)
>>> res
5
>>> def sum(a,b=0):
	return a+b

>>> res=sum(2)
>>> res
2
>>> 
============= RESTART: C:/Users/rajin/Desktop/jan 19/function.py =============
Enter namerajin
>>> 
>>> 
============= RESTART: C:/Users/rajin/Desktop/jan 19/function.py =============
Enter namerajin
>>> 
>>> 
============= RESTART: C:/Users/rajin/Desktop/jan 19/function.py =============
>>> 
============= RESTART: C:/Users/rajin/Desktop/jan 19/function.py =============
>>> 
============= RESTART: C:/Users/rajin/Desktop/jan 19/function.py =============
Happy Birthday to you Happy Birthday to you Happy Birthday dearRajin Happy Birthday to you
>>> 
============= RESTART: C:/Users/rajin/Desktop/jan 19/function.py =============
Enter namerajin
Happy Birthday to you 
 Happy Birthday to you 
 Happy Birthday dearname 
 Happy Birthday to you
>>> 
============= RESTART: C:/Users/rajin/Desktop/jan 19/function.py =============
Enter namerajin
Happy Birthday to you 
 Happy Birthday to you 
 Happy Birthday dearx 
 Happy Birthday to you
>>> 
>>> 
>>> 
>>> def name(nam="RAJIN"):
	print("Your name is ",nam)

	
>>> def(rajin)
SyntaxError: invalid syntax
>>> name()
Your name is  RAJIN
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def sum(*args);
SyntaxError: invalid syntax
>>> def sum(*args):
	print(args)

	
>>> sum()
()
>>> sum(1)
(1,)
>>> sum(,1,2,3,4,5,6)
SyntaxError: invalid syntax
>>> sum(1,2,3,4,5,6,)
(1, 2, 3, 4, 5, 6)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def sum_numbers(*args):
	return sum(args)

>>> sum_numbers()
((),)
>>> sum_numbers(1,3,4)
((1, 3, 4),)
>>> 

>>> def sum_vals(**kwarg):
	print(kwargs)

	
>>> 
>>> sum_vals()
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    sum_vals()
  File "<pyshell#134>", line 2, in sum_vals
    print(kwargs)
NameError: name 'kwargs' is not defined
>>> def sum_vals(**kwargs):
	print(kwargs)

	
>>> sum_vals()
{}
>>> sum_vals(a=1,b=8)
{'a': 1, 'b': 8}
>>> 
sdas
Traceback (most recent call last):
  File "<pyshell#141>", line 2, in <module>
    sdas
NameError: name 'sdas' is not defined
>>> x
'ajin'
>>> r
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    r
NameError: name 'r' is not defined
>>> a
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> v
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    v
NameError: name 'v' is not defined
>>> b
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> d
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    d
NameError: name 'd' is not defined
>>> x
'ajin'
>>> x
'ajin'
>>> x
'ajin'
>>> x
'ajin'
>>> x
'ajin'
>>> x
'ajin'
>>> x
'ajin'
>>> x
'ajin'
>>> x
'ajin'
>>> x
'ajin'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 



>>> 

>>> 



>>> 

>>> 



>>> 

>>> 



>>> 

>>> 



>>> 

>>> 


>>> 
>>> 
