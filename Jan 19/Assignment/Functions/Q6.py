'''
6. Write a Python function that accepts a string and calculate the number of upper case letters
and lower case letters.
Sample String : 'The quick Brow Fox'

Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
'''

def count_string(text):
    upper_case = 0
    lower_case = 0
    for each in text:
        if 'a' <= each <= 'z':
            lower_case += 1
        elif 'A' <= each <= 'Z':
            upper_case += 1

    print(f"No. of Upper case characters: {upper_case}")
    print(f"No. of Lower case charactersL {lower_case}")

st_ring = "Ram Is going To sea"
count_string(st_ring)
