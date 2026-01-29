"""
LAmbda function:
    - A small anonymous function for a one time use. They take any number of arguments but have only 1 expression
    - Helps keep namespace clean and is useful with higher order functions like sort(), map(), filter(), reduce()
    - syntax: lambda paramter(s): expression
"""

double = lambda x: x*2
add = lambda x,y: x+y
max_value = lambda x,y: x if x > y else y
min_value = lambda x,y: x if x < y else y
full_name = lambda first,last: first + " " + last
is_even = lambda x:x%2 == 0
age_check = lambda x: True if x > 21 else False

print(double(2))
print(add(2,3))