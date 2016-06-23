###NT_MAX/10 >= sum和INT_MAX - digit >= sum这两个判断条件确保了不会溢出。
#Notes for Soluton1 
#chr()根据整数返回对应的字符，也就是讲ascii转换为字符
#unichr()将整数返回成unicode字符
#ord（）将字符转换成ascii码

class Solution(object):
      def myAtoi(self, str):
        INT_MAX = 2147483647; INT_MIN = -2147483648
        sum = 0
        sign = 1
        i = 0
        if str == '':
            return 0
        while i < len(str) and str[i].isspace():
            i += 1
        if i < len(str) and str[i] == '-':
            sign = -1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            i += 1
        while i < len(str) and str[i].isdigit():
            digit = int(str[i])
            if INT_MAX/10 >= sum:
                sum *= 10
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            if INT_MAX - digit >= sum:
                sum += digit
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            i += 1
        return sign*sum

    