


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n >=1 :
            return n & (n-1) == 0
        else:
            return False


