class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        if len(nums) == 0:
            return results
        self.dfs(nums, [] , 0 ,results)
        return results
    
    def search(self, nums, path, index, results):
        if path not in results:
            results.append(path)
        for i in range(index, len(nums)):
            self.search(nums, path+[nums[i]], i+1 ,results)