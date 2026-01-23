"""
Link to problem on LeetCode: https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i = 0
    j = len(height)-1
    res = 0
    while i<j:
        a = (j - i) * min(height[i],height[j])
        res = max(res,a)
        if height[i] < height[j]:
            i+=1
        else:
            j-=1
    return res

x = [1,8,6,2,5,4,8,3,7]
output = maxArea(x)
expected = 49
print("Test case 1:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )

x = [1,1]
output = maxArea(x)
expected = 1
print("Test case 2:")
print(f"Input: {x} | Expected: {expected} | Actual: {output} | Results: ", "Pass" if output == expected else "Fail" )