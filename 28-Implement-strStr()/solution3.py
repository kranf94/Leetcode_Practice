class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ##Subtring 的做法
        if haystack is None or needle is None:
            return -1
        for i in xrange (len(haystack) - len(needle) +1):
            if haystack[i : i +len(needle)] == needle:
                return i
        return -1