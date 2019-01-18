'''
Q.4 Get the first name and last name from a user and use different string formatting techniques that we
learnt in class to get a formatted string.
For example: If user’s first name is Ram and last name is Bahadur, the output should be:
Hello! Ram Bahadur.

Author: Rajin Maharjan
Date: 2019-01-15
'''

first_name=input("Enter your first name:")
last_name=input("Enter your last name :")
print("Hello!",first_name, last_name)
print("Hello! {} {}".format(first_name,last_name))
print("Hello! {0} {1}".format(first_name,last_name))
print("Hello! {f_name} {l_name}".format(f_name=first_name,l_name=last_name))
print(f"Hello! {first_name} {last_name}")
