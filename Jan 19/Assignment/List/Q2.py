'''
2. Write a Python program to count the number of strings where the string length is 2 or more
and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

num = int(input("Enter number of items in the list: "))
li_st = []
for each in range(num):
    strings = input("Enter string: ")
    li_st.append(strings)
count = 0
for each in li_st:
    if len(each) >= 2 and each[0] == each[len(each)-1]:
        count += 1
print(f"{count}")
