//
// Created by zhuhonglin on 2020/11/25.
//
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int rst = 0;
        for (int i=0; i<nums.size(); ++i) {
            int cnt = 0;
            for (int j=i; j<nums.size();++j) {
                cnt += nums[j];
                if (cnt >= lower and cnt <= upper) {
                    rst++;
                }
            }
        }
        return rst;
    }
};

int main() {
    vector<int> nums = {-2, 5, -1};
    cout << Solution().countRangeSum(nums, -2, 2) << endl;
    return 0;
}
