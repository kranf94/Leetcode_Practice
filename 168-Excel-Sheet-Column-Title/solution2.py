class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result =''
        while n>0 :
          
                result = chr(ord('A') + (n-1) %26) +result
                n = (n -1 )/26
                
        return result;
               
    #n=26 n-1=25 直接避免了第一种方法里面 ==0 需要调取Z 的情况
            