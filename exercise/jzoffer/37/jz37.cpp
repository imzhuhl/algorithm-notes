//
// Created by zhuhonglin on 2020/11/25.
//

#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        queue<TreeNode *> q1;
        string rst = "";
        TreeNode *p = root, *q = nullptr;
        q1.push(p);
        while (!q1.empty()) {
            q = q1.front();
            q1.pop();
            if (q) {
                rst.append(to_string(q->val));
                q1.push(q->left);
                q1.push(q->right);
            } else {
                rst.push_back('$');
            }
            rst.push_back(',');
        }
        return rst;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        string numstr = "";
        vector<TreeNode *> node_arr;
        int i = 0;
        while (i<data.size()) {
            if (data[i] == ',') {
                int val = stoi(numstr);
                TreeNode *tmp = new TreeNode(val);
                node_arr.push_back(tmp);
                numstr = "";
            } else if (data[i] == '$') {
                node_arr.push_back(nullptr);
                i++;
            } else {
                numstr.push_back(data[i]);
            }
            i++;
        }

        int j=1;
        TreeNode *root = node_arr[0];
        for (int i=0; i<node_arr.size(); ++i) {
            TreeNode *p = node_arr[i];
            if (p) {
                p->left = node_arr[j++];
                p->right = node_arr[j++];
            }
        }
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));

int main() {
    Codec codec;
    codec.deserialize("1,2,3,$,$,4,5,$,$,$,$,");
    return 0;
}