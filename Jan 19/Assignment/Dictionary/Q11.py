'''
11. Write a Python program to sort a dictionary by key.
'''
import operator
dic1 = {
    'Anime': "Noragami",
    'Release date': "6th December 2010",
    'Genre': 'Occult Fiction',
    
}

dic2={}

dic2 = sorted(dic1.items(), key=operator.itemgetter(0))
print(f"Ascending ordered dictionary:\n {dic2}")


