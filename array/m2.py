class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            c=abs(x)-1
            a=nums[c]
            if a < 0:
                res.append(c+1)
            else:
                nums[c]*=-1
        return res

# similar approach based on hashmap within an array marking visited ones as negative