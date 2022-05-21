#User function Template for python3

class Solution:

    def findPair(self, arr, L,N):
        #code here
        arr.sort()
        size = L
        
        # Initialize positions of two elements
        i,j = 0,1
        
        # Search for a pair
        while i < size and j < size:
        
            if i != j and arr[j]-arr[i] == N:
                print(arr[j],arr[i])
                return 1
        
            elif arr[j] - arr[i] < N:
                j+=1
            else:
                i+=1
        return -1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Ends