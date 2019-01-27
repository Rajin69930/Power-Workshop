'''
8. Write a Python program to sum all the items in a dictionary.
'''


dic1 = {
    1:5,
    2:25,
    3:125
    
}

dic2 = {
    'Anime Movie':"Kimi no nawa",
    'Movie': "A Quiet Place"
}

sum_dic=0

for val in dic1.values():
    sum_dic += val
print(f"The sum of all the values is : {sum_dic}")

sum_dic = ""
for val in dic2.values():
    sum_dic += val
print(f"The sum of all the values is : {sum_dic}")
