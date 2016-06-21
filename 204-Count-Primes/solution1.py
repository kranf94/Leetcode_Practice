
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
         x=2
         while x*x<n:
               if isPrimes[x]:
                   p=x*x
                   while p<n :
                   isPrimes[p]= False
                   p=x+p
               x=x+1   
         return sum(isPrimes)