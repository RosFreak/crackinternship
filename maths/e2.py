class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        carry =0
        ans = ""
        n = max(len(a),len(b))
        for i in range(n+1):
                try:
                    val = int(a[i:i+1]) + int(b[i:i+1]) + carry
                except:
                    try:
                        val = int(a[i:i+1]) + carry
                    except:
                        try:
                            val = int(b[i:i+1]) + carry
                        except:
                            val =carry
                if (val) == 3:
                    ans += "1"
                    carry =1
                elif (val ) == 2:
                    ans += "0"
                    carry =1
                else:
                    ans += str(val)
                    carry =0
        ans = ans[::-1]
        if ans[0] == "0":
            return ans[1:]
        return ans