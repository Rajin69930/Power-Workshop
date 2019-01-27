'''
8. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
'''
list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
highest_sum = 0
highest = 0
for x, list2 in enumerate(list1):
    sum_list = 0
    for each in list2:
        sum_list += each
    if sum_list > highest_sum:
        highest_sum = sum_list
        highest = x
print(f"The list in a list of lists whose sum of elements is the highest is : {list1[highest]}")
