class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}
        n = len(nums)
        for i in range(n):
            if ( nums[i] ) in l:
                return [l[nums[i]],i]
            l[ target - nums[i] ] = i
