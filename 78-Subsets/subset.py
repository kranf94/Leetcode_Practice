class Solution(object):
    def subsets(self, nums):
        res = []
        nums.sort()
        for i in range(1<<len(nums)):
            tmp= []
            for j in rage(len(nums)):
                if i & 1 << j:
                    tmp.append(nums[j])
            res.append(temp)
        return res