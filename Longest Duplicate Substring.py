#Longest Duplicate Substring

class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        sa,rk = [],[]
        for i in xrange(n):
            rk.append(ord(S[i])-ord('a'))
            sa.append(i)
        l,sig = 0,26
        while True:
            p = []
            for i in xrange(n-l,n):
                p.append(i)
            for i in xrange(n):
                if sa[i]>=l:
                    p.append(sa[i]-l)
            cnt = [0]*sig
            for i in xrange(n):
                cnt[rk[i]] += 1
            for i in xrange(1,sig):
                cnt[i] += cnt[i-1]
            for i in xrange(n-1,-1,-1):
                cnt[rk[p[i]]] -= 1
                sa[cnt[rk[p[i]]]] = p[i]
            def equal(i,j,l):
                if rk[i]!=rk[j]:return False
                if i+l>=n and j+l>=n:
                    return True
                if i+l<n and j+l<n:
                    return rk[i+l]==rk[j+l]
                return False
            sig = -1
            tmp = [None]*n
            for i in xrange(n):
                if i==0 or not equal(sa[i],sa[i-1],l):
                    sig += 1
                tmp[sa[i]] = sig
            rk = tmp
            sig += 1
            if sig==n:
                break
            l = l<<1 if l>0 else 1
        maxh = k = 0
        idx = None
        for i in xrange(n):
            if rk[i]>0:
                j = sa[rk[i]-1]
                while i+k<n and j+k<n and S[i+k]==S[j+k]:
                    k += 1
                if k>maxh:
                    maxh = k
                    idx = i
                if k>0:
                    k -= 1
        return S[idx:idx+maxh] if idx!=None else ""