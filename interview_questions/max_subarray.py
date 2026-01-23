"""
Given an array of integers nums, write a function max_subarray(nums) that finds the contiguous subarray (containing at least one number) with the largest sum and returns its sum.

Remember to also account for an array with 0 items.



Function Signature:

def max_subarray(nums):


Input:

A list of integers nums.



Output:

An integer representing the sum of the contiguous subarray with the largest sum.



Example:

max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
Output: 6
Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum, which is 6.
"""


# WRITE THE MAX_SUBARRAY FUNCTION HERE #
#                                      #
#                                      #
#                                      #
#                                      #
########################################
def max_subarray(nums):
    if len(nums) == 0:
        return 0
    currSum = nums[0]
    maxSum = nums[0]
    for num in nums[1:]:
        currSum = max(num,currSum + num)
        maxSum = max(maxSum, currSum)        
    return maxSum

# Example 1: Simple case with positive and negative numbers
input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = max_subarray(input)
expected=6
print(f"Input: {input} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )

# Example 2: Case with a negative number in the middle
input = [1, 2, 3, -4, 5, 6]
output = max_subarray(input)
expected=13
print(f"Input: {input} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )

# Example 3: Case with all negative numbers
input = [-1, -2, -3, -4, -5]
output = max_subarray(input)
expected=-1
print(f"Input: {input} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )


"""
    EXPECTED OUTPUT:
    ----------------
    Example 1: Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    Result: 6
    Example 2: Input: [1, 2, 3, -4, 5, 6] 
    Result: 13
    Example 3: Input: [-1, -2, -3, -4, -5] 
    Result: -1
    
"""