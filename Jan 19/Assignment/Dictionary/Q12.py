'''
12. Write a Python program to get the maximum and minimum value in a dictionary.
'''

dic1 = {
    'A': 19,
    'B': 58,
    'C': 100,
    'D': 12,
    'E': 10,
    'F': 1
}

maxvalue = max(dic1.keys(), key=lambda a: dic1[a])
minvalue = min(dic1.keys(), key=lambda a: dic1[a])
print(f"Minimum value is: {dic1[minvalue]}")
print(f"Maximum value is: {dic1[maxvalue]}")
