'''
5. Write a function called digit_sum that can take any mumber of integer arguments takes returns
the sum of all that number's digits.
'''
def digit_sum(*args):
    sum = 0
    for each in args:
        sum += each
    return sum

print(digit_sum(1,56,8,9,78,6))

