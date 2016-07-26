class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result =''
        while n>0 :
            if n%26 == 0 :
                result ='Z' +result
                n= n/26 -1
            else:
                result = chr(ord('A') +n%26 -1) +result
                n = n/26
                
        return result;
               
    
            