###解题思路：将罗马数字转换成对应的整数。首先将罗马数字翻转，从小的开始累加，如果遇到CM（M-C=1000-100=900）这种该怎么办呢？因为翻转过来是MC，M=1000先被累加，所以使用一个last变量，把M记录下来，如果下一个数小于M，那么减两次C，然后将C累加上，这个实现比较巧妙简洁。

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map= {"M": 1000, "D":500, "C":100, "L":50 ,"X":10, "V":5, "I":1}
        sum=0
       
       
        last=None
        
        for i in xrange (len(s)) :
             if i>0 and roman_map[s[i]] >roman_map[s[i-1]] :
                sum += -2*roman_map[s[i-1]]+roman_map[s[i]]
             else:
                sum += roman_map[s[i]]
 
        return sum

        
                