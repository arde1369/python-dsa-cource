"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    closestSumToTarget = 0
    currentLowestDist = float('inf')
    for left in range(len(nums)-2):
        mid = left+1
        right = len(nums)-1
        while mid < right:
            currSum = nums[left]+nums[mid]+nums[right]
            dist = abs(currSum-target) #calculate current distance from the sum of current triplet from target
            if dist < currentLowestDist:
                currentLowestDist = dist
                closestSumToTarget = currSum
            if currSum < target: #increment mid pointer to get closer to target since list is sorted
                mid+=1
            elif currSum > target: #decrement right pointer to get closer to target since list is sorted
                right-=1
            else: #If current sum is equal to target then we cant get any closer so we return current sum
                return currSum
    return closestSumToTarget

x = [-1,2,1,-4]
output = threeSumClosest(x,1)
expected = 2
print("Test case 1:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )

x = [0,0,0]
output = threeSumClosest(x,1)
expected = 0
print("Test case 2:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )