'''
3. Write a Python program to get a string from a given string where all occurrences of its first
char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''

st_ring = input("Enter a string: ")

new_list = list()
new_list.append(st_ring[0])
for each in st_ring[1:]:
    if each == st_ring[0]:
        new_list.append('$')
    else:
        new_list.append(each)
new_string = "".join(new_list)
print(new_string)
