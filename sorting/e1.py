#User function Template for python3

class Solution:
    def isPossible(self,a, b, n, k):
        a.sort()
        b.sort(reverse = True)
        c=0
        for i in range(n):
            if a[i] + b[i] >= k:
                continue
            c=1
            break
        if(c==1):
            return False
        return True




