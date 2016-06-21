
# Time:  O(n)
# Space: O(n)
import math from sqrt

class Solution(object):
     def countPrimes(self, n):
        """
         :type n: int
         :rtype: int
         """
        if n<=2:
            return 0
        
        isPrimes= [True]*n
        isPrimes[0],isPrimes[1] = False, False
        
        num = 0 
        sqr = sqrt(n-1)
        
        for i in xrange(2,sqr):
               if isPrimes[i]:
                   num += 1
                   for j in xrange ( i +1, n, i):
                       isPrimes[j]= False
                       
        return num