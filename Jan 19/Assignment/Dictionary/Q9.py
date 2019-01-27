'''
9. Write a Python program to multiply all the items in a dictionary.
'''
dic = {
    1:5,
    2:25,
    3:125
    
}
mul_val=1
for val in dic.values():
    mul_val*=val
print(f"The product of all the values is : {mul_val}")    
