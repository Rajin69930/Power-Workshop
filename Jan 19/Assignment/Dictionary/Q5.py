'''
5. Write a Python program to iterate over dictionaries using for loops.
'''

dic1 = {
    'Anime': "Noragami",
    'Release date': "6th December 2010",
    'Genre': 'Occult Fiction',
    
}
for key, val in dic1.items():
    print(f"{key} : {val}")


dic2 = {
    'Anime Movie':"Kimi no nawa",
    'Movie': "A Quiet Place"
}
for key, val in dic2.items():
    print(f"{key} : {val}")
