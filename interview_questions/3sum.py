"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    res = []
    for l in range(0, len(nums)-2): #iterates through list and sets left pointer. len(nums)-2 makes sure we always have a mid and right pointers
        #Makes sure we dont have duplicates so it skips any duplicates that are next to each other.Skips until last occurence.
        if l > 0 and nums[l] == nums[l-1]:
            continue
        m = l+1 #mid pointer
        r = len(nums)-1 #right pointer
        while m < r: 
            s = nums[l]+nums[m]+nums[r]
            if s < 0: 
                m+=1
            elif s > 0:
                r-=1
            else:
                res.append([nums[l],nums[m],nums[r]])
                while m < r and nums[m] == nums[m+1]: #skips all duplicates from middle
                    m+=1
                while m < r and nums[r] == nums[r-1]: #skips all duplicates from right
                    r-=1
                m+=1
                r-=1
    return res

x = [-1,0,1,2,-1,-4]
output = threeSum(x)
expected = [[-1,-1,2],[-1,0,1]]
print("Test case 1:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )

x = [0,1,1]
output = threeSum(x)
expected = []
print("Test case 2:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )

x = [0,0,0]
output = threeSum(x)
expected = [[0,0,0]]
print("Test case 3:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )