#include <iostream>
using namespace std;

struct Node {
    int val_;
    Node *left_, *right_;
    Node(int val): val_(val), left_(nullptr), right_(nullptr) {}
};
int postorder[35];
int inorder[35];


Node* build(int in_l, int in_r, int post_l, int post_r) {
    if (post_l >= post_r || in_l >= in_r) {
        return nullptr;
    }
    int val = postorder[post_r-1];
    int idx = -1;
    for (int i = in_l; i < in_r; ++i) {
        if (inorder[i] == val) {
            idx = i;
            break;
        }
    }
    Node* node = new Node(val);
    node->left_ = build(in_l, idx, post_l, post_l + idx - in_l);
    node->right_ = build(idx+1, in_r, post_l + idx - in_l, post_r - 1);
    return node;
}


int main() {
    int n;
    scanf("%d", &n);

}