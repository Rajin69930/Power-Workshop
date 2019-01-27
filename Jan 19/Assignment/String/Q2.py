'''
2. Write a Python program to count the number of characters (character frequency)
in a string.Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''

st_ring = input("Enter a string: ")
string_dict = {}
for each in st_ring:
    string_dict[each] = st_ring.count(each)
print(string_dict)
