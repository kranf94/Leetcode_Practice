# Time:  O(n)
# Space: O(1)


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX= (2<<30)-1
        INT_MIN= -1*INT_MAX -1
        
        result = 0
        while i < len(str) and str[i] == " " :
             i += 1
        
        sign =1
        if str[i] == "+" :
           i +=1
        else str[i] == "-":
           i += 1
           sign = -1
          
        while i< len (str) and str[i] >='0' and str[i] <='9' :
            if result > (INT_MAX - (ord(str[i]) -ord(str[0])))/10     ###返回对应的ASCII数值
               return INT_MAX if sign >0 else INT_MIN
            result =result*10 +ord(str[i]) -ord(str[0])
            i +=1
        return sign*result
        