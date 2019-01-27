'''
7. Write a Python program to check the validity of password input by users.
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].

At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
'''
character = ('$', "#", '@')
char_1 = False
char_2 = False
char_3 = False
char_4 = False
length = False


password = input("Enter password: ")

for each in password:
    if 'a' <= each <= 'z':
        char_1 = True
    elif '0' <= each <= '9':
        char_2 = True
    elif 'A' <= each <= 'Z':
        char_3 = True
    else:
        for new in character:
            if new == each:
                char_4 = True

if 6 <= len(password) <= 16:
    length = True

if char_1 and char_2 and char_3 and char_4 and length:
    print("Password is valid.")
else:
    print("Invalid password.")
