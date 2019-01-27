'''
3. Write a Python program to check whether an element exists within a tuple.
'''

x= (10,100,1000,100000,99999,999,99,9)
element = int(input("Enter a element: "))
print(f"The element exists within the tuple: { element in x }")
