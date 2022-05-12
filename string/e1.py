class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        f=0
        for i in s:
            if i in ['[','(','{']:
                l.append(i)
            else:
                try:
                    if (l[len(l)-1] == '(') and (i == ')'):
                        l.pop()
                    elif (l[len(l)-1] == '[') and (i == ']'):
                        l.pop()
                    elif (l[len(l)-1] == '{') and (i == '}'):
                        l.pop()
                    else:
                        f=1
                        break
                except:
                    f=1
                    break
        if l==[] and f==0:
            return True
        else:
            return False

# stack 