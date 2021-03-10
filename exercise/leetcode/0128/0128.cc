#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> us;
        for (int i = 0; i < nums.size(); ++i) {
            us.insert(nums[i]);
        }
        
        int max_len = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (us.find(nums[i]-1) == us.end()) {
                int cnt = 0;
                int v = nums[i];
                while (us.find(v) != us.end()) {
                    ++cnt;
                    ++v;
                }
                max_len = max(max_len, cnt);
            }
        }
        return max_len;
    }
};