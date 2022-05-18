class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        s= ""
        c = 0
        try:
            flag =1
            while(flag):
                base = strs[0][c]
                for i in strs:
                    if i[c] != base:
                        flag =0
                        break
                if(flag):
                    s+=i[c]
                    c+=1
        except:
            pass
        return s
            