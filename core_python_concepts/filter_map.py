"""
map() and filter() return iterators in Python 3, so you often wrap them in list() to see the results immediately.
"""
numbers = [1, 2, 3, 4, 5, 6]

# 1. filter() with lambda: Keep only even numbers
#    Output: [2, 4, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

# 2. map() with lambda: Square the even numbers
#    Output: [4, 16, 36]
squared = list(map(lambda x : x * x, even))

print(squared)

#I have a list (iterable) of my favourite pet names, all in lower case and I need them in uppercase
my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(lambda x : x.upper(), my_pets))
print(uppered_pets)