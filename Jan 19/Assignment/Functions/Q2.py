'''
2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
'''
def get_sum(a):
    sum = 0
    for each in a:
        sum += each
    return sum

li_st = list()
numb_list = int(input("Enter no of numbers: "))
for i in range(numb_list):
    numbers = int(input("Enter number: "))
    li_st.append(numbers)
print(f"Number list {li_st}")    
print(f"The sum of all the numbers in list is : {get_sum(li_st)}")
