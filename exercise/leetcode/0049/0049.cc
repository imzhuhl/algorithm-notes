#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<int>> tb;

        for (int i = 0; i < strs.size(); ++i) {
            string tmp = strs[i];
            sort(tmp.begin(), tmp.end());
            tb[tmp].push_back(i);
        }

        vector<vector<string>> rst;
        for (auto it = tb.begin(); it != tb.end(); ++it) {
            vector<string> tmp;
            vector<int>& info = it->second;
            for (int i = 0; i < info.size(); ++i) {
                tmp.push_back(strs[info[i]]);
            }
            rst.emplace_back(move(tmp));
        }

        return rst;

    }
};