class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        ref: https://www.youtube.com/watch?v=Ca7k53qcTic
        """
        nums.sort()
        triplets = []
        n = len(nums)
        
        # Only iterate up to n-2 (skip two item), because those two
        # items will be j, k in the last iteration
        for i in range(n-2): 
            # If nums[i] == nums[i-1], all the triplets that includes
            # nums[i] were already found. (i==0 avoid nums[-1] error)
            if i == 0 or nums[i] != nums[i-1]:
                ####Highlight####
                # We start to find two number that sums up equal to -x
                # We fix x, and look at all the items behind it.
                # j += 1 --> sum increases
                # k -= 1 --> sum reduces
                # the while loop in the if logic is simply skipping 
                # the same numbers that we just found.
                j, k = i + 1, n - 1
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    if s == 0:
                        triplets.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        while j < k and nums[k] == nums[k-1]:
                            k -= 1
                        j, k = j + 1, k - 1
                    elif s > 0:
                        k -= 1
                    else:
                        j += 1
        return triplets
 

# My original Code
# Train of thoughts:
# Fix one number first(x), and then go through the number behind it
# and find two numbers that is -x when summed up
"""
class Solution(object):
    def threeSum(self, nums):
        triplets = []
            for idx, x in enumerate(nums):
                for idy, y in enumerate(nums[idx+1:]):
                    z = -x - y
                    tmp = [x, y, z]
                    tmp.sort()
                    if z in nums[idx+idy+2:] and tmp not in triplets:
                        triplets += [tmp]
              
            return triplets
"""