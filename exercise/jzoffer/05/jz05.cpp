//
// Created by zhuhonglin on 2020/11/25.
//

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string replaceSpace(string s) {
        char st[40000]{'\0'};
        int p = 0;
        for (char c: s) {
            if (c == ' ') {
                st[p++] = '%';
                st[p++] = '2';
                st[p++] = '0';
            } else {
                st[p++] = c;
            }
        }
        return string(st);
    }
};

int main() {
    string s = "We are happy";
    cout << Solution().replaceSpace(s) << endl;
    return 0;
}