class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0 :
          return 0 
        return (num-1)%9+1
        
        
        """
        in  out  in  out
0   0    10  1
1   1    11  2
2   2    12  3
3   3    13  4
4   4    14  5
5   5    15  6
6   6    16  7
7   7    17  8
8   8    18  9
9   9    19  1
可以发现输出与输入的关系为：

out = (in - 1) % 9 + 1