#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        vector<int> max_dp(nums);
        vector<int> min_dp(nums);
        for (int i = 1; i < nums.size(); ++i) {
            int v1 = nums[i]*max_dp[i-1];
            int v2 = nums[i]*min_dp[i-1];
            max_dp[i] = max(nums[i], max(v1, v2));
            min_dp[i] = min(nums[i], min(v1, v2));
        }
        return *max_element(max_dp.begin(), max_dp.end());
    }
};
