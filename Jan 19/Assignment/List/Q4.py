'''
4. Write a Python program to create a list by concatenating a given list which range goes from 1
to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''

num = int(input("Enter No. of items in the list: "))
li_st = []
for each in range(num):
    items = input("Enter item: ")
    li_st.append(items)
new_list = []
x = int(input("Enter a number: "))
for each in range(1, x+1):
    for new in li_st:
        new_list.append(new + str(each))
print(f"New list: {new_list}")
