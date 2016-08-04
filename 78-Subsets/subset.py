class Solution(object):
    def search(self, nums, S, index):
        if index == len(nums):
            self.results.append(S)
            return
        self.search(nums, S+[nums[index]], index+1)
        self.search(nums, S, index+1)
     
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.results=[]
        self.search(sorted(nums), [], 0)
        return self.results