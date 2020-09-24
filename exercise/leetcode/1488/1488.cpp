
#include <iostream>
#include <vector>
#include <set>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        vector<int> rst(rains.size(), 1);
        set<int> zero;
        unordered_map<int, int> lake_day;

        for (int i = 0; i < rains.size(); ++i) {
            int k = rains[i];

            if (k == 0) {
                zero.insert(i);
                continue;
            }

            if (lake_day.count(k) == 1) {
                auto it = zero.lower_bound(lake_day[k]);
                if (it == zero.end()) return {};
                rst[*it] = k;
                zero.erase(it);
            }

            lake_day[k] = i;
            rst[i] = -1;
        }
    }
};
    

    
