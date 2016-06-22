
###解题思路：将罗马数字转换成对应的整数。首先将罗马数字翻转，从小的开始累加，如果遇到CM（M-C=1000-100=900）这种该怎么办呢？因为翻转过来是MC，M=1000先被累加，所以使用一个last变量，把M记录下来，如果下一个数小于M，那么减两次C，然后将C累加上，这个实现比较巧妙简洁。

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map= {"M": 1000, "D":500, "C":100,"L":50 , "X":10, "V":5, "I":1}
        
        s=s[::-1]
        ###Define the last node to store the value used to compare
        
        last=None
        for x in s :
             if last and roman_map[x]<last :
                sum -= -2*roman_map[x]
             sum += roman_map[x]
             last=roman_map[x]
        return sum
        
                