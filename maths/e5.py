class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while (not((n==1) or (n in seen))):
            c=n
            seen.add(n)
            ans = 0
            while(c!=0):
                r = c%10
                ans+= r**2
                c = c//10
            n = ans
        if n==1:
            return True
        return False
            

# Better solution floyd cycle detection