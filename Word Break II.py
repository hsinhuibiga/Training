#Word Break II

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        memo = dict()
        return self.dfs(s, res, wordDict, memo)

    def dfs(self, s, res, wordDict, memo):
        if s in memo: return memo[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)] != word: continue
            for r in self.dfs(s[len(word):], res, wordDict, memo):
                res.append(word + ("" if not r else " " + r))
        memo[s] = res
        return res