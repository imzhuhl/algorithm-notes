//
// Created by zhuhonglin on 2020/11/25.
//

#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    int findNthDigit(int n) {
        if (n <= 9) {
            return n;
        }
        int head = 10;
        long base = 10;
        int digit = 2;
        while (true) {
            long tmp = head + 9 * base * digit;
            if ((long)n < tmp) {
                break;
            }
            head = tmp;
            digit++;
            base *= 10;
        }

        int rest = n - head;
        int rst_num = base + rest / digit;
        int rst_dig = rest % digit;
        string rst_str = to_string(rst_num);
        return rst_str[rst_dig] - '0';
    }
};

int main() {
    cout << Solution().findNthDigit(1000000000) << endl;
    return 0;
}