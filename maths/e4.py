class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        s=""
        while(n!=0):
            r = n%26
            if (r == 0):
                r =26
                n -= 1
            s+=chr(r+64)
            n = n//26
        return s[::-1]