
class Solution:
    def decodeString(self, s: str) -> str:
        """栈
        """
        st = []
        num = []
        for i, v in enumerate(s):
            if v.isdigit():
                num.append(v)
            elif v == '[':
                st.append(int(''.join(num)))
                st.append(v)
                num = []
            elif v == ']':
                part = []
                while st[-1] != '[':
                    part.append(st.pop())
                st.pop()  # pop '['
                k = st[-1]
                st.pop()  # pop 'k'
                part.reverse()
                part = part * k
                st.extend(part)
            else:
                st.append(v)

        return ''.join(st)


if __name__ == '__main__':
    s = '10[a]2[bc]'
    sl = Solution()
    print(sl.decodeString(s))
