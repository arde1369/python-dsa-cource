class Solution(object):
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        wp = 1
        count = 0
    
        for rp in range(1, len(nums)):
            if nums[rp] != nums[rp-1]:
                count = 0
            else:
                count += 1

            if count < 2:
                nums[wp] = nums[rp]
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
