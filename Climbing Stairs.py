#Climbing Stairs

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre = cur = 1
        for i in xrange(1, n):
            pre, cur = cur, pre+cur
        return cur