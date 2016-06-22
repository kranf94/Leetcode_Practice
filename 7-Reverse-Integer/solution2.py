# Time: O(logn)
# Space: O(1)

class Solution:
    # @return an integer
      def reverse(self, x):
        answer = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        while x > 0:
            answer = answer * 10 + x % 10
            x /= 10
        return sign*answer if answer <= 2147483647 else 0   ###Handle the overflow