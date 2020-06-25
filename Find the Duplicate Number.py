#Find the Duplicate Number

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = left + (right - left)/2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid :
                    count += 1
            if count > mid :
                right = mid - 1
            else:
                left = mid + 1
        return left
