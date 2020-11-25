//
// Created by zhuhonglin on 2020/11/25.
//

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        int i = int(matrix.size()) - 1;
        int j = 0;
        while (i >= 0 and j < matrix[0].size()) {
            if (target == matrix[i][j]) {
                return true;
            } else if (target < matrix[i][j]) {
                i--;
            } else { // target > matrix[i][j]
                j++;
            }
        }
        return false;
    }
};
