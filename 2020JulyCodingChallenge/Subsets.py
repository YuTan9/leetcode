class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subset = []
        length = 2**len(nums)
        for i in range(length):
            onehot = self.binary(i)
            toAppend = []
            for index, item in enumerate(onehot):
                if item == 1:
                    toAppend.append(nums[index])
            subset.append(toAppend)
        return subset
            
    # def binary(self, length, digit):
    #     forReturn = [0] * length
    #     for i in range(length-1, -1, -1):
    #         forReturn[i] = digit % 2
    #         digit = digit // 2
    #         if digit == 0:
    #             break
    #     return forReturn

    def binary(self, digit):
        forReturn = []
        if digit == 0:
            return [0]
        while digit != 0:
            forReturn.append(digit%2)
            digit = digit // 2

        return forReturn
