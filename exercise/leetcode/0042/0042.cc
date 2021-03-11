#include <vector>
#include <algorithm>
#include <stack>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        stack<int> st;
        int cnt = 0;
        for (int i = 0; i < height.size(); ++i) {
            while (!st.empty() && height[st.top()] < height[i]) {
                int a = height[st.top()];
                st.pop();
                if (st.empty()) continue;
                int li = st.top();
                int mh = min(height[i], height[li]);
                cnt += (mh - a) * (i - li - 1);
            }
            st.push(i);
        }
        return cnt;
    }
};