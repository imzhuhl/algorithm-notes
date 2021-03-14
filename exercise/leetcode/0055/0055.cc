#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int len = nums.size();
        vector<int> dp(len, 0);
        dp[0] = 1;
        for (int i = 1; i < len; ++i) {
            for (int j = i-1; j >= 0; --j) {
                if (dp[j] == 1 and j + nums[j] >= i) {
                    dp[i] = 1;
                    break;
                }
            }
        }
        return dp[len-1] == 1 ? true : false;
    }
};