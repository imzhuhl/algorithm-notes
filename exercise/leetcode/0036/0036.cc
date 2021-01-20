#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int rows[9][10] = {0};
        int cols[9][10] = {0};
        int block[9][10] = {0};

        for (int i=0; i<9; ++i) {
            vector<char>& line = board[i];
            for (int j=0; j<9; ++j) {
                char v = line[j];
                if (v == '.') continue;
                int val = v - '0';

                if (rows[i][val] == 1) return false;
                rows[i][val] = 1;

                if (cols[j][val] == 1) return false;
                cols[j][val] = 1;

                int block_idx = i / 3 + 3 * (j / 3);
                if (block[block_idx][val] == 1) return false;
                block[block_idx][val] = 1;
            }
        }
        return true;
    }
};