'''
Suppose the cover price of a book is Rs. 240, but bookstores get a
40% discount. Shipping costs Rs. 25 for the first 20 copies and
Rs. 15 for each additional copy. What is the total wholesale cost
for 60 copies?

Author : Rajin Maharjan
Date: 2019-01-15
'''

discount=40
first_copyprice=25
additional_copyprice=15

num_copy=int(input("Enter number of books :"))
cover_price=int(input("Enter the cover price of a book :"))

total_discount=num_copy*(discount/100)*cover_price

if(num_copy<=20):
    total_price=first_copyprice*num_copy
elif(num_copy>20):
    total_price=(first_copyprice*20)+((num_copy-20)*additional_copyprice)

wholesale_cost=(cover_price*num_copy)-total_discount+total_price

print("The total wholesale cost for 60 copies is :",wholesale_cost)


