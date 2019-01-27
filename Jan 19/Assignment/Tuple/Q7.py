'''
7. Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
'''

list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list2 = []
for each in list1:
    list3 = list(each)
    list3[-1] = 100
    x = tuple(list3)
    list2.append(x)
print(list2)
