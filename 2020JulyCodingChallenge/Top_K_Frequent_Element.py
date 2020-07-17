class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dictionary = dict()
        for idx, num in enumerate(nums):
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        
        arr = []
        
        for i in range(k):
            max, idx = -1, -1
            for key in dictionary:
                if dictionary[key] > max:
                    max = dictionary[key]
                    idx = key
            arr.append(idx)
            dictionary[idx] = -1
            
        
        return arr




"""
counter = collections.defaultdict(lambda: 0)
for num in nums:
    counter[num] += 1

q = []
for num, freq in counter.iteritems():
    heapq.heappush(q, (-freq, num))

results = []
for i in range(k):
    _, num = heapq.heappop(q)
    results.append(num)
return results
"""