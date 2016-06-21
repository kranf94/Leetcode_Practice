
# Time:  O(n)
# Space: O(n)
###Still need to figoure out how to use sqrt to reduce the time limition

from math import sqrt

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        
        num = 0
        for i in xrange(2, n):
            if is_prime[i]:
               num += 1
               for j in xrange(i+i, n, i):
                   is_prime[j] = False
                   
        return num
        
####Check http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n for more solutions#####