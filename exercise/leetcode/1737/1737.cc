#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int minCharacters(string a, string b) {
        int cta[26] = {0};
        int ctb[26] = {0};
        for (int i = 0; i < a.size(); ++i) {
            cta[int(a[i])-97] += 1;
        }
        for (int i = 0; i < b.size(); ++i) {
            ctb[int(b[i])-97] += 1;
        }

        int total = a.size() + b.size();
        int best = total;
        int sa = 0, sb = 0, tmp = 0;
        for (int i = 0; i < 25; ++i) {
            sa += cta[i];
            sb += ctb[i];
            int t1 = (int)a.size() - sa + sb;
            int t2 = total - cta[i] - ctb[i];
            int t3 = sa + (int)b.size() - sb;
            tmp = min({t1, t2, t3});
            best = best > tmp ? tmp : best;
        }
        tmp = total - cta[25] - ctb[25];

        return min(best, tmp);
    }
};