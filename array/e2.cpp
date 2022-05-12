class Solution {
public:
    void sortColors(vector<int>& nums) {
        int red=0;
        int green=0;
        int n=0;
        for(auto i=nums.begin();i!=nums.end();i++){
            if(*i == 0) red++;
            else if(*i == 1) green++;
            n++;
        }
        for(int i=0;i<n;i++){
            if (i<red) nums[i] = 0;
            else if(i < red+green) nums[i] = 1;
            else nums[i] = 2;
        }
        
    }
};


//solution based on count sort
//better solution will be Dutch national flag