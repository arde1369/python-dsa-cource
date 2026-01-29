from functools import singledispatch

@singledispatch
def process_data(data):
    print(f"This is a generic type {type(data)} :: {data}")

@process_data.register(int)
def _(data):
    print(f"data is an integer: {data}")

@process_data.register(float)
def _(data):
    print(f"data is a float: {data}")

@process_data.register(str)
def _(data):
    print(f"data is a string: {data}")

@process_data.register(list)
def _(data):
    print(f"data is a list: {data}")

process_data(10)
process_data([1, 2, 3])
process_data("hello world")
process_data(4.5)
process_data((1,2))