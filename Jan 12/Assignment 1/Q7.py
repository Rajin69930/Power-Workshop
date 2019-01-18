"""
Q7. Write a function called disect that takes a list, modifies it by removing the first and
last elements
For example:
>>> l = [1, 2, 3, 4]
>>> disect(t)
>>> t
[2, 3]
Author: Rajin Maharjan
Date: 2019-01-15
"""
def disect(a):
    a.remove(a[0])
    if(len(a)-1>0):
        a.remove(a[len(a)-1])
    return a

li_st = list()

n = int(input("Enter the number of elements in list: "))


for x in range(n):
    b = input("Enter an element to insert in list: ")
    li_st.append(b)

print("Original List: {}".format(li_st))

li_st = disect(li_st)
print("Modified List: {}".format(li_st))    



