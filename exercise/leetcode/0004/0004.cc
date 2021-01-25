#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size();
        int len2 = nums2.size();
        if (len1 > len2) return findMedianSortedArrays(nums2, nums1);
        if (len1 == 0) return (nums2[(len2-1)/2] + nums2[len2/2]) * 1.0 / 2;
        int total_len = len1 + len2;
        int start1 = 0, end1 = len1;
        int cur1, cur2;
        while (start1 <= end1) {
            cur1 = (start1 + end1) / 2;
            cur2 = (total_len+1) / 2 - cur1;
            double l1 = (cur1 == 0) ? numeric_limits<int>::min() : nums1[cur1-1];
            double r1 = (cur1 == len1) ? numeric_limits<int>::max() : nums1[cur1];
            double l2 = (cur2 == 0) ? numeric_limits<int>::min() : nums2[cur2-1];
            double r2 = (cur2 == len2) ? numeric_limits<int>::max() : nums2[cur2];
            if (l1 > r2) {
                end1 = cur1 - 1;
            } else if (l2 > r1) {
                start1 = cur1 + 1;
            } else {
                if (total_len % 2 == 1) {
                    return max(l1, l2);
                } else {
                    return (max(l1, l2) + min(r1, r2)) / 2;
                }
            }
        }
        return 0.0;
    }
};

int main() {
    vector<int> nums1 = {3};
    vector<int> nums2 = {-2, -1};
    Solution solution;
    cout << solution.findMedianSortedArrays(nums1, nums2) << endl;

    return 0;
}

