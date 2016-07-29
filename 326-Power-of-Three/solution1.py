class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
    ###求对数，然后乘方，判断是否相等
        return n >0 and 3 **round(math.log(n,3)) == n 
