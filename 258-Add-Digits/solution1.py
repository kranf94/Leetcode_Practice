class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
     
        while num >9 :  
            result = 0 
            while num:
               result = num %10 +result
               num = num /10 
            num = result
            
        return result
        