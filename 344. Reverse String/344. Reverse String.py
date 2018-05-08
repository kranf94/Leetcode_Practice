# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:19:58 2018

@author: jpan
"""
#344. Reverse String
#8种方法的比较:
#1. 简单的步长为-1, 即字符串的翻转(常用);
#2  Built in Function reversed() 
#3. 先转化为list，倒序成功之后，再join
#4. 交换前后字母的位置;
#5. 递归的方式, 每次输出一个字符;
#6. 双端队列, 使用extendleft()函数;
#7. 使用for循环, 从左至右输出;
#8. 依次交换前面和后面的字符直至中间字符，完成反转。需要注意Python不能直接修改字符串的某一位，所以需要先转成字符串数组再处理。该思路也用双指针实现。


a = 'hello'

#Solution1
a[::-1]

a[1:4]
a[1:4:2]#Move Forward 2 positions

#Solution2
''.join(reversed(a))

#''.join(reversed(a.strip().split()))

#Strip()Returns a copy of the string with the leading and trailing characters removed.

#Solution3 
l = list(a)
l.reverse()
''.join(l)

#Solution4
t = list(a)
lg = len(t)

for i, j in zip(range(lg-1,0,-1),range(lg//2)):
    t[i],t[j] = t[j], t[i]
''.join(t)

#Solution5
def string_reverse5(string):  
    if len(string) <= 1:  
        return string  
    return string_reverse5(string[1:]) + string[0]  

string_reverse5(a)

#Soliton6
from collections import deque 
d = deque()  
d.extendleft(a) 
''.join(d)

#Soliton7
''.join(a[i] for i in range(len(a)-1, -1, -1)) 

#Solution8 
#Similar to Solution 4 but only use on pointer
s = list(a)
for i in range(0,len(s)//2,1):
    tmp = s[i]
    s[i] = s[len(s)-1-i]
    s[len(s)-1-i] = tmp
''.join(s)

#Solution9
#Similar to Solution 5 but using the half part not all of them
def reverseString(s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        left_s = s[:len(s)//2]
        right_s = s[len(s)//2:]
        return reverseString(right_s) + reverseString(left_s)

reverseString(a)
