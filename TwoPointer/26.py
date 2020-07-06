class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 1
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                length += 1
                nums[length-1] = nums[i]
                
        return length