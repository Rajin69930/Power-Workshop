'''
3. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''

def edit_list(new_list):
    if len(new_list)-1 >= 5:
        del new_list[5]
    if len(new_list)-1 >= 4:
        del new_list[4]
    if len(new_list)-1 >= 0:
        del new_list[0]
    return new_list
num = int(input("Enter number of items in the list: "))
li_st = []
for each in range(num):
    item = input("Enter item: ")
    li_st.append(item)
print(f"New list: {edit_list(list_1)}")
