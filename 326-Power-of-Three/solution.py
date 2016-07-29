class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n % 3 == 0 :
                n = n/3
        return True
    