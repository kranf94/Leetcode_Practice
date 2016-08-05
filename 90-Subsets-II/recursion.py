class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = [[]]
        for num in sorted(nums):
            results = results +[i +[num] for i in results if i +[num] not in results]
        return results
       