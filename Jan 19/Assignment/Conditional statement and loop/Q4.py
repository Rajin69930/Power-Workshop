'''
4. Write a Python program to count the number of even and odd numbers from a series of
numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
'''
numbs = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for each in numbs:
    if each % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Number of even numbers: {even}")
print(f"Number of even numbers: {odd}")
