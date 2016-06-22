# Time:  O(n)
# Space: O(1)

###解法更直接 利用index####

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map= {"M": 1000, "D":500, "C":100, "L":50 ,"X":10, "V":5, "I":1}
        sum=0
       
       
        last=None
        
        for i in xrange (len(s)) :  ###range return a list but xrange just the 调用
             if i>0 and roman_map[s[i]] >roman_map[s[i-1]] :
                sum += -2*roman_map[s[i-1]]+roman_map[s[i]]
             else:
                sum += roman_map[s[i]]
 
        return sum

        
                