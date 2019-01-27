'''
13. Write a Python program to remove duplicates from Dictionary.
'''

dic1 = {
    'Anime1': {'hinamatsuri'},
    'Anime2': {'noragami'},
    'Anime3': {'dragon ball Z'},
    'Anime4': {'hinamatsuri'},
    'Anime5': {'noragami'}
}
dic2={}

for key, val in dic1.items():
    repeated_val = False
    for each in dic2.values():
        if each == val:
            repeated_val = True
    if not repeated_val:
        dic2[key] = val
print(dic2)
