#3Sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = collections.Counter(nums)
        values = count.keys()
        values.sort()
        print(values)
        N = len(values)
        l, r = 0, N - 1
        res = list()
        visited = set()
        for l in range(N):
            for r in range(l, N):
                t = 0 - values[l] - values[r]
                if t in count:
                    if (t == 0 and count[t] >= 3) \
                    or (((t == values[l] and t != values[r]) or (t == values[r] and t != values[l])) and count[t] >= 2) \
                    or (l == r and values[l] != t and count[values[l]] >= 2) \
                    or (t != values[l] and t != values[r] and l != r):
                        curlist = sorted([values[l], t, values[r]])
                        finger = "#".join(map(str, curlist))
                        if finger not in visited:
                            res.append(curlist)
                            visited.add(finger)
        return res
