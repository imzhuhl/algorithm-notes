#include <vector>
#include <unordered_map>
#include <stack>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegree(numCourses, 0);
        unordered_map<int, vector<int>> road;
        for (int i = 0; i < prerequisites.size(); ++i) {
            road[prerequisites[i][1]].push_back(prerequisites[i][0]);
            indegree[prerequisites[i][0]] += 1;
        }
        
        vector<int> visited(numCourses, 0);
        stack<int> st;
        for (int i = 0; i < indegree.size(); ++i) {
            if (indegree[i] == 0) {
                st.push(i);
                visited[i] = 1;
            }
        }

        while (!st.empty()) {
            int id = st.top();
            st.pop();
            vector<int>& lst = road[id];
            for (int i=0; i<lst.size(); ++i) {
                indegree[lst[i]] -= 1;
                if (indegree[lst[i]] == 0) {
                    st.push(lst[i]);
                    visited[i] = 1;
                }
            }
        }

        for (int i : visited) {
            if (i == 0) {
                return false;
            }
        }
        return true;

    }
};