class Solution {
public:
    // optimized 
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for(int i = 0; i < nums.size(); i++){
            int diff = target - nums[i];
            if(seen.count(diff)){
                return{seen[diff], i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }

    /* 
    // brute force 
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> targetNums;
        for(int i = 0; i < nums.size() - 1; i++){
            for(int j = i + 1; j < nums.size(); j++){
                if(nums[i] + nums[j] == target){
                    targetNums.push_back(i);
                    targetNums.push_back(j);
                }
            }
        }
        return targetNums;
    }
    */ 
};