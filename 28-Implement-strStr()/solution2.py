class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        for i in range(len(haystack) - len(needle)+1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                   break
            else:
                return i
        else:
            return -1