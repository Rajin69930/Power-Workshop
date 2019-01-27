'''
1. Write a Python program to sum all the items in a list.
    Do not use built-in sum() function.
'''

num = int(input("Enter number of items in the list: "))
li_st = []
for each in range(num):
    item = int(input("Enter item: "))
    li_st.append(item)
sum_items = 0
for each in li_st:
    sum_items += each
print(li_st)    
print(f"the sum of all the items in the list is : {sum_items}")
