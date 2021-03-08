#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;


// 慢速，暴力递归
class Solution1 {
public:
    string longestPalindrome(string s) {
        int len = s.size();
        for (int off = len-1; off >= 0; --off) {
            for (int j = 0; j+off < len; ++j) {
                bool ret = check(s, j, j+off);
                if (ret) return s.substr(j, off+1);
            }
        }
        return NULL;
    }
    
    bool check(string& s, int i, int j) {
        if (i >= j) {
            return true;
        }
        if (s[i] == s[j]) {
            return check(s, i+1, j-1);
        } 
        return false;

    }
};


// 带记忆，动态规划
class Solution2 {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));

        for (int i = 0; i < n; ++i) {
            dp[i][i] = 1;
        }
        for (int i = 0; i < n-1; ++i) {
            if (s[i] == s[i+1]) {
                dp[i][i+1] = 1;
            }
        }

        for (int j = 2; j < n; ++j) {
            for (int i = 0; i+j < n; ++i) {
                if (s[i] == s[i+j]) {
                    dp[i][i+j] = dp[i+1][i+j-1];
                }
            }
        }

        for (int j = n-1; j >= 0; --j) {
            for (int i = 0; i + j < n; ++i) {
                if (dp[i][i+j] == 1) {
                    return s.substr(i, j+1);
                }
            }
        }

        return NULL;
    }
};