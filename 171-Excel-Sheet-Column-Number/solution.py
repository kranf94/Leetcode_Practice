class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        for char in s :
             result = (ord(char) - ord('A')+1) +result*26    #*26 26的倍数
        return result ;