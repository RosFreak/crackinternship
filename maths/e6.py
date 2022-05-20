class Solution:
    def isPalindrome(self, x: int) -> bool:
        m=x
        rev=0
        if x>=0:
            while(m!=0):
                rev= rev*10 + (m%10)
                m=m//10
            if x==rev:
                return True
        return False
