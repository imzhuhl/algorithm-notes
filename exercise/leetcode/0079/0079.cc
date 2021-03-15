#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        vector<vector<int>> visited(board.size(), vector<int>(board[0].size(), 0));
        char h = word[0];
        for (int i = 0; i < board.size(); ++i) {
            for (int j = 0; j < board[i].size(); ++j) {
                if (board[i][j] == h) {
                    bool tmp = dfs(i, j, 0, board, word, visited);
                    if (tmp) return true;
                }
            }
        }
        return false;
    }

    bool dfs(int i, int j, int k, vector<vector<char>>& board, string& word, vector<vector<int>>& visited) {
        if (k >= word.size()) return true;
        if (i < 0 || i >= board.size()) return false;
        if (j < 0 || j >= board[i].size()) return false;
        if (visited[i][j] == 1) return false;
        
        visited[i][j] = 1;

        if (board[i][j] == word[k]) {
            bool t1 = dfs(i+1, j, k+1, board, word, visited);
            bool t2 = dfs(i-1, j, k+1, board, word, visited);
            bool t3 = dfs(i, j+1, k+1, board, word, visited);
            bool t4 = dfs(i, j-1, k+1, board, word, visited);
            if (t1 || t2 || t3 || t4) {
                return true;
            }
        }
        visited[i][j] = 0;
        return false;
    }

};

int main() {
    vector<vector<char>> board {{'A', 'B', 'C', 'E'}, {'S','F','C','S'}, {'A','D','E','E'}};
    string word = "ABCCED";
    cout << Solution().exist(board, word) << endl;
    return 0;
}


