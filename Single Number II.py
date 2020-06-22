
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        counts = [0] * 32
        res = 0
        for i in range(0, 32):
            for num in nums:
                #num = long(num)
                counts[i] += (num>>i) & 1
            res |= ((counts[i] % 3) << i)
        if 0 != counts[31] % 3:
            res -= pow(2, 32)
        return res