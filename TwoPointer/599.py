class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        common = []
        ranking= 3000
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i+j < ranking:
                        ranking = i+j
                        common = [list1[i]]
                    elif i+j == ranking:
                        common = common + [list1[i]]
        return common


"""
class Solution(object):
    def findRestaurant(self, list1, list2):
        ids = dict()
        for idx, word in enumerate(list1):
            ids[word] = idx
            
        best_sum = len(list1) + len(list2)
        best = []
        for idx, word in enumerate(list2):
            if word in ids: 
                curr_sum = ids[word] + idx
                if curr_sum == best_sum:
                    best.append(word)
                elif curr_sum < best_sum:
                    best_sum = curr_sum
                    best = [word]
                    
        return best
"""