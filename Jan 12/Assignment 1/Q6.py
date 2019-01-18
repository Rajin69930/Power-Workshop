"""
Q6.Write a python script to demonstrate at least 10 built in functions in Python.
Author: Rajin Maharjan
Date: 2019-01-15
"""
x=int(input("Enter a number for it's absolute value :"))
value=abs(x)
print("It's absolute value is :",value)
print("The boolen function of {} is {}".format(x,bool([x])))

y=float(input("Enter a number :"))
z=float(input("Enter the power :"))
po_wer=pow(y,z)
print("Ans :",po_wer)


a=int(input("Enter a number to convert into binary, octal and hexadecimal :"))
oc_t=oct(a)
he_x=hex(a)
bi_n=bin(a)
print("The binary form is :",bi_n)
print("The octal form is :",oc_t)
print("The hexadecimal form is :",he_x)

string=input("Enter a string :")
print("The length of string is :{}".format(len(string)))

list_name=[1,3,5,7,9,11]
print("Initial list of odd numbers form 1-11 is :",list_name)
print("Sliced list of odd numbers is :{}".format(slice(1,4)))

b=int(input("Enter first number :"))
c=int(input("Enter second number :"))
print("It's complex form is :{}".format(complex(b,c)))
print("b//c and b%c= {}".format(divmod(b,c))) 
