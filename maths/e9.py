class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        return n==2**(int(math.log2(n)))