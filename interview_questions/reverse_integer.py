"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

Constraints:

-231 <= x <= 231 - 1
"""

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    #Convert to String
    s = str(x)

    #Check if numer was a negative
    if s[0] == "-":
        #If Negative Omit from from the beginning of the string
        s= s[1:]

        #Flip the string -> 's[::-1]' 
        #Add negative sign back in -> '"-" +'
        #Strip any leading zeros -> .lstrip("0")
        s=("-" +s[::-1]).lstrip("0")
    else:
        #Flip the string -> 's[::-1]' 
        #Strip any leading zeros -> .lstrip("0")
        s = (s[::-1]).lstrip("0")
    
    #Check if reveresed integer meets constraints -231 <= x <= 231 - 1
    if -2**31 <= int(s) <= 2**31 - 1:
        return int(s)
    return 0


x = 120
output = reverse(x)
expected = 21
print("Test case 1:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )

x = 123
output = reverse(x)
expected = 321
print("Test case 2:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )

x = -123
output = reverse(x)
expected = -321
print("Test case 3:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )

x = 1534236469
output = reverse(x)
expected = 0
print("Test case 4:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )