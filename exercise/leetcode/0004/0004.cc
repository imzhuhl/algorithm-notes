#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size();
        int len2 = nums2.size();
        if (len1 > len2) return findMedianSortedArrays(nums2, nums1);
        int total_len = len1 + len2;
        int cur1, cur2;

        if (len1 == 0) {
            int mid = total_len / 2;
            if (total_len % 2 == 1) return static_cast<double>(nums2[mid]);
            else return (static_cast<double>(nums2[mid]) + static_cast<double>(nums2[mid-1])) / 2;
        }

        helper(nums1, nums2, total_len / 2 + 1, cur1, cur2);

        if (total_len % 2 == 1) {
            return static_cast<double>(max(nums1[cur1], nums2[cur2]));
        }

        int a, b;
        if (nums1[cur1] > nums2[cur2]) {
            a = nums1[cur1];
            cur1 -= 1;
        } else {
            a = nums2[cur2];
            cur2 -= 1;
        }
        if (cur1 < 0) b = nums2[cur2];
        else if (cur2 < 0) b = nums1[cur1];
        else if (nums1[cur1] > nums2[cur2]) b = nums1[cur1];
        else b = nums2[cur2];

        return (a+b) * 1.0 / 2;
    }

    void helper(vector<int>& nums1, vector<int>& nums2, int k, int& cur1, int& cur2) {
        int left1 = 0, right1 = nums1.size() - 1;
        int idx1, idx2;
        while (true) {
            idx1 = (left1 + right1) / 2;
            idx2 = k - (idx1 + 1) - 1;

            if (idx2+1 < nums2.size() && nums1[idx1] > nums2[idx2+1]) {
                right1 = idx1 - 1;
            } else if (idx1+1 < nums1.size() && nums2[idx2] > nums1[idx1+1]) {
                left1 = idx1 + 1;
            } else {
                cur1 = idx1;
                cur2 = idx2;
                break;
            }
        }
    }
};

int main() {
    vector<int> nums1 = {3};
    vector<int> nums2 = {-2, -1};
    Solution solution;
    cout << solution.findMedianSortedArrays(nums1, nums2) << endl;

    return 0;
}

