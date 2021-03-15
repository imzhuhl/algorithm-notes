class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> need;
        int cur_need = 0;
        for (int i = 0; i < t.size(); ++i) {
            need[t[i]]++;
            cur_need++;
        }

        int left = 0;
        int right = 0;
        int min_len = 100000;
        int rst_l, rst_r;

        while (true) {
            while (right < s.size() && cur_need > 0) {
                if (need.find(s[right]) != need.end()) {
                    if (need[s[right]] > 0) cur_need--;
                    need[s[right]]--;
                }
                right++;
            }
            if (cur_need != 0) {
                break;
            }
            while (cur_need == 0) {
                if (min_len > right - left) {
                    min_len = right - left;
                    rst_l = left;
                    rst_r = right;
                }
                if (need.find(s[left]) != need.end()) {
                    if (need[s[left]] >= 0) cur_need++;
                    need[s[left]]++;
                }
                left++;
            }
        }

        if (min_len == 100000) {
            return string();
        }
        return s.substr(rst_l, rst_r - rst_l);


    }
};