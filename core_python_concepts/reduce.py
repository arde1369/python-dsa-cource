"""
reduce() function (from functools) applies a function cumulatively to an iterable, reducing it to a single value. 
It’s handy for concise tasks like summing, multiplying (factorial), finding max/min, concatenating strings or flattening lists.
"""
from functools import reduce

a = [1, 2, 3, 4, 5]
sum = reduce(lambda x,y : x + y, a)

print(sum)

words = ["Geeks", "for", "Geeks", "is", "for", "geeks"]
sentence = reduce(lambda x, y: x + " " +y, words)
print(sentence)
