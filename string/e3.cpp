class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.length();
        int m = needle.length();
        int flag=-1;
        for(int i=0;i<n;i++){
            if (haystack[i] == needle[0]){
                flag=1;
                for(int j=1;j<m;j++){
                    if ((i+j) < n)
                    if (haystack[i+j] == needle[j]){
                        continue;
                    }
                    flag=-1;
                }
                if(flag ==1){
                    return i;
                }
            }
        }
        return -1;
    }
};

// normal brute force solution