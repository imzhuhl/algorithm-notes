#include <iostream>
#include <vector>
#include <array>
#include <queue>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> graph(numCourses, vector<int>(numCourses, 0));
        vector<int> indegree(numCourses, 0);

        for (int i = 0; i < prerequisites.size(); ++i) {
            int start = prerequisites[i][1];
            int end = prerequisites[i][0];
            graph[start][end] = 1;
            indegree[end] += 1;
        }

        queue<int> s;
        for (int i = 0; i < numCourses; ++i) {
            if (indegree[i] == 0) {
                s.push(i);
            }
        }

        vector<int> rst;
        while (!s.empty()) {
            int n = s.front();
            s.pop();
            rst.push_back(n);
            for (int i = 0; i < numCourses; ++i) {
                if (graph[n][i] != 0) {
                    graph[n][i] = 0;
                    indegree[i]--;
                    if (indegree[i] == 0) {
                        s.push(i);
                    }
                }
            }
        }

        if (rst.size() == numCourses) {
            return true;
        }
        return false;
    }
};


int main() {
    cout << "hello" << endl;
}
