'''
1. Write a Python program to add an item in a tuple.
'''

x = ()
numb = int(input("Enter the number of items: "))
for i in range(numb):
    items = input("Enter item to be added: ")
    x = x + (items,)
print(f"{x}")
