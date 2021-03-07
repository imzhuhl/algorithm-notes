#include <iostream>
#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        stack<int> day;
        vector<int> rst(T.size(), 0);
        for (int i = 0; i < T.size(); ++i) {
            while (!day.empty() && T[i] > T[day.top()]) {
                int idx = day.top();
                rst[idx] = i - idx;
                day.pop();
            }
            day.push(i);
        }

        return rst;
    }
};