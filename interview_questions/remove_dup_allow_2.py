class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        wp = 1
        count = 0
    
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count = 0
            else:
                count += 1

            if count < 2:
                nums[wp] = nums[i]
                wp += 1

        return wp
    
solution =Solution()
nums = [1,1,1,2,2,3]
print("test case 1:")
print("nums before: ", nums)
result = solution.removeDuplicates(nums)
print("nums after: ",nums[:result])

nums = [0,0,1,1,1,1,2,3,3]
print("test case 2:")
print("nums before: ", nums)
result = solution.removeDuplicates(nums)
print("nums after: ",nums[:result])
