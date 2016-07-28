class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
    
        numSet= set()
        ###两重while 用numSet 记录每次得到的平房和 当出现非1的重复平房和时，返回False
        while n !=1 and n not in numSet:
             numSet.add(n) #Add an element to a set
             sum = 0
             while n :
                 digit = n%10
                 sum += digit *digit # powe(digit,2)
                 n = n/10
             n = sum
            
        return n == 1
