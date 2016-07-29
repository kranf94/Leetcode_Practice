class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num == 0 or num % 4 >0 :
            return False
        return self.isPowerOfFour(num/4)