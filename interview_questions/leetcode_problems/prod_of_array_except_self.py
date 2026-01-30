"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    answer = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    
    for i in range(n):
        answer[i] = prefix[i] * suffix[i]
    
    return answer

x = [1,2,3,4]
expected = [24,12,8,6]
output = productExceptSelf(x)
print("Test case 1:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )

x = [-1,1,0,-3,3]
expected = [0,0,9,0,0]
output = productExceptSelf(x)
print("Test case 2:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )