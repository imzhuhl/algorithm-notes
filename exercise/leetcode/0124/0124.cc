#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        int max_val = -1000;
        dfs(root, max_val);
        return max_val;
    }

    int dfs(TreeNode* root, int& max_val) {
        if (!root) {
            return 0;
        }
        int lv = max(0, dfs(root->left, max_val));
        int rv = max(0, dfs(root->right, max_val));
        int cv = root->val;

        max_val = max(max_val, cv+lv+rv);
        
        return cv + max(lv, rv);

    }
};