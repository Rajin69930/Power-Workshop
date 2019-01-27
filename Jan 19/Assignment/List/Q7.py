'''
7. Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
'''

li_st = [1, 2, 3, 4]
x = 0
for each in li_st:
    li_st[x] = 'emp' + str(each)
    x += 1
print(f"New list: {li_st}")
