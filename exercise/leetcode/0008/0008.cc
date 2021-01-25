#include <iostream>
#include <string>
#include <cctype>
#include <climits>
using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        int i = 0;
        int sign = 1;
        long rst = 0;
        while (str[i] == ' ') ++i;
        
        if (str[i] == '-' || str[i] == '+') {
            if (str[i] == '-') sign = -1;
            ++i;
        }

        if (!isdigit(str[i])) return 0;

        while (i < str.size()) {
            if (!isdigit(str[i])) break;
            rst = rst * 10 + (str[i] - '0');
            if (sign == 1 && rst > INT_MAX) {
                return INT_MAX;
            } else if (sign == -1 && -1 * rst < INT_MIN) {
                return INT_MIN;
            }
            ++i;
        }

        return (int) sign * rst;
    }
};

int main() {
    string str = "-342";
    Solution s;
    cout << s.myAtoi(str) << endl;
    return 0;
}
