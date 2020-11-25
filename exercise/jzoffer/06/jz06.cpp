//
// Created by zhuhonglin on 2020/11/25.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    vector<int> reversePrint(ListNode* head) {
        vector<int> rst;
        ListNode *p = head;
        while (p != nullptr) {
            rst.push_back(p->val);
            p = p->next;
        }
        reverse(rst.begin(), rst.end());
        return rst;
    }
};
