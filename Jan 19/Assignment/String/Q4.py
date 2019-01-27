'''
4. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given
string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''
st_ring = input("Enter a string: ")
new_string = str()
if len(st_ring) < 3:
    print(st_ring)
else:
    if st_ring[-3:] == "ing":
        new_string = st_ring + "ly"
    else:
        new_string = st_ring + "ing"
print(new_string)
