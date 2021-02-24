#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        flip1(matrix);
        flip2(matrix);
    }

    void flip1(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i <= n-1; ++i) {
            for (int j = 0; j <= n-1-i; ++j) {
                int tmp = matrix[i][j];
                    swap(matrix[i][j], matrix[n-1-j][n-1-i]);
            }
        }
    }

    void flip2(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i < n / 2; ++i) {
            for (int j = 0; j < n; ++j) {
                swap(matrix[i][j], matrix[n-1-i][j]);
            }
        }
    }
};