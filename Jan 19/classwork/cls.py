Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def mix(a,b=10,*args,**kwargs);
SyntaxError: invalid syntax
>>> def mix(a,b=10,*args,**kwargs):
	print(a,b,args,kwargs)

	
>>> mix(1)
1 10 () {}
>>> mix(1,b=815)
1 815 () {}
>>> 

>>> mix(1,15,True,False,p=100,q=200)
1 15 (True, False) {'p': 100, 'q': 200}
>>> 
>>> 
>>> 
>>> l=[1,2,3]
>>> def f(ll):
	del ll[0]

	
>>> l
[1, 2, 3]
>>> f(l)
>>> l
[2, 3]
>>> l
[2, 3]
>>> 
f(l.copy())
>>> 
>>> l
[2, 3]
>>> 
>>> 


>>> 


>>> 

>>> 



>>> 

>>> 

>>> s="print('Hello World')"
>>> eval(s)
Hello World
>>> 
>>> 



>>> 

>>> 



>>> 

>>> 
>>> eval("Rajin * 10")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    eval("Rajin * 10")
  File "<string>", line 1, in <module>
NameError: name 'Rajin' is not defined
>>> eval("'Rajin' * 10")
'RajinRajinRajinRajinRajinRajinRajinRajinRajinRajin'
>>> 
