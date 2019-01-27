'''
10. Write a Python program to remove a key from a dictionary.
'''


dic1 = {
    'Anime': "Noragami",
    'Release date': "6th December 2010",
    'Genre': 'Occult Fiction',
    
}

print(dic1)

x=input("Enter a key present in the dictionary :")

if x in dic1:
    del dic1[x]
    print(dic1)

else:
        print("Invalid Key")
