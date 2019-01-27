'''
7. Write a Python script to merge two Python dictionaries.
'''


dic1 = {
    'Anime': "Noragami",
    'Release date': "6th December 2010",
    'Genre': 'Occult Fiction',
    
}

dic2 = {
    'Anime Movie':"Kimi no nawa",
    'Movie': "A Quiet Place"
}

dic3={}
dic3.update(dic1)
dic3.update(dic2)
print(dic3)
    
