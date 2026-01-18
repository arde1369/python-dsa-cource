class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



## WRITE REVERSE_STRING FUNCTION HERE ###
#                                       #
#  This is a separate function that is  #
#  not a method within the Stack class. #
#  Indent all the way to the left.      #
#                                       #
#########################################
def reverse_string(s):
    if len(s) > 0:
        stack = Stack()
        for idx in range(0,len(s)):
            stack.push(s[idx])
        reversedString = ""
        while stack.peek():
            reversedString+=stack.pop()
        return reversedString
    else:
        return ""


my_string = 'hello'

print ( reverse_string(my_string) )



"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
