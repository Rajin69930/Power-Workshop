'''
1. Write a Python script to sort (ascending and descending) a dictionary by
    value.
'''

dictionary = {}
num = int(input("How many entries you want? :"))
for i in range(num):
    entry = input("Enter entry: ")
    dictionary[i] = entry
print(f"Dictionary : {dictionary}")
ordered_dictionary = sorted(dictionary.items(), key=lambda a: a[1])
print(f"Ascending ordered dictionary: {ordered_dictionary}")
reverse = sorted(dictionary.items(), key=lambda b: b[1], reverse=True)
print(f"Descending order dictionary: {reverse}")
