'''
1. Write a Python program to calculate the length of a string.
    Do not use built-in len() function.
'''

st_ring = input("Enter a String: ")
len_st_ring = 0
for each in st_ring:
    len_st_ring += 1
print(f"The length of string {st_ring} is : {len_st_ring}")
