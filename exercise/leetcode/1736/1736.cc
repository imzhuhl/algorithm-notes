#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string maximumTime(string time) {
        char h1 = time[0];
        char h2 = time[1];
        char m1 = time[3];
        char m2 = time[4];

        if (h1 == '?') {
            if (h2 == '?' || (h2 - '0') < 4) h1 = '2';
            else h1 = '1';
        }
        if (h2 == '?') {
            h2 = (h1 == '2') ? '3' : '9'; 
        }
        if (m1 == '?') m1 = '5';
        if (m2 == '?') m2 = '9';

        time[0] = h1;
        time[1] = h2;
        time[3] = m1;
        time[4] = m2;
        return time;
    }
};
