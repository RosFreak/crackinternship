class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        diff =[0 for i in range(n-1)]
        for i in range(n-1):
            diff[i] = prices[i+1] - prices[i]
        sum =0
        max =0
        for i in diff:
            sum += i
            if sum > max :
                max = sum
            if sum < 0:
                sum=0
        return max

# Kadane algorithm