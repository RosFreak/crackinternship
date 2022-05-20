class Solution:
    def reverse(self, x: int) -> int:
        m=abs(x)
        rev=0
        while(m!=0):
            rev= rev*10 + (m%10)
            m=m//10
        if x==0:
            return 0
        ans = rev * (x//abs(x))
        return ans if ans < 2**31 and ans >= -2**31 else 0