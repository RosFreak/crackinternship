class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int dup = -1;
        for (int i = 0; i < nums.size(); i++) {
            int cur = abs(nums[i]);
            if (nums[cur] < 0) {
                dup = cur;
                break;
            }
            nums[cur] *= -1;
        }
        
        // Restore numbers
        for (auto& num : nums)
            num = abs(num);
        
        return dup;
    }
};


// Hash map within an array
//marking visited numbers as negative