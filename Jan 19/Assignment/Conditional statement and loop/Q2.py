"""
2. Create a for loop that prompts the user for a hobby 3 times,
   then appends each one to hobbies.
  
"""

hobby = list()
for x in range(3):
    x = input("Enter your hobby: ")
    hobby.append(x)
print(f"Your hobbies are: {hobby}")
