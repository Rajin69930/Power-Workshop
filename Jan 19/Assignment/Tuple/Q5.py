'''
5. Write a Python program to remove an item from a tuple.
'''
x = (5,10,15,20,25,30,35,40,45,50)
print(x)
item = int(input("enter a item to remove from a tuple: "))
li_st = list(x)
li_st.remove(item)
x = tuple(li_st)
print(x)
