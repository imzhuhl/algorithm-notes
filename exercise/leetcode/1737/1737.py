
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        psa = [0 for _ in range(26)]
        psb = [0 for _ in range(26)]

        for c in a:
            psa[ord(c)-97] += 1
        for c in b:
            psb[ord(c)-97] += 1

        for i in range(1, 26):
            psa[i] += psa[i-1]
            psb[i] += psb[i-1]
        
        total_len = len(a) + len(b)
        best = total_len
        for ia in range(26):
            less_a = psa[ia-1] if ia > 0 else 0
            for ib in range(26):
                less_b = psb[ib-1] if ib > 0 else 0
                if ia < ib:
                    tmp = (psa[-1] - psa[ia]) + less_b
                elif ia == ib:
                    tmp = less_a + less_b + (psa[-1] - psa[ia]) + (psb[-1] - psb[ib])
                else:  # ia > ib
                    tmp = less_a + (psb[-1] - psb[ib])

                if best > tmp:
                    best = tmp
        return best


class Solution2:
    def minCharacters(self, a: str, b: str) -> int:
        cta = [0 for _ in range(26)]
        ctb = [0 for _ in range(26)]

        for c in a:
            cta[ord(c)-97] += 1
        for c in b:
            ctb[ord(c)-97] += 1

        
        total_len = len(a) + len(b)
        best = total_len
        sa, sb = 0, 0
        for i in range(25):
            sa += cta[i]
            sb += ctb[i]
            # a < b
            t1 = len(a) - sa + sb
            # a == b
            t2 = total_len - cta[i] - ctb[i]
            # a > b
            t3 = sa + len(b) - sb
            
            tmp = min(t1, t2, t3)
            if best > tmp:
                best = tmp
        
        tmp = total_len - cta[25] - ctb[25]

        return min(best, tmp)


if __name__ == '__main__':
    a = "dabadd"
    b = "cda"
    print(Solution2().minCharacters(a, b))
