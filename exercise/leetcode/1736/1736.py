class Solution:
    def maximumTime(self, time: str) -> str:
        h1, h2 = time[0], time[1]
        m1, m2 = time[3], time[4]
        if h1 == "?":
            h1 = "2" if h2 == "?" or int(h2) < 4 else "1"
        if h2 == "?":
            h2 = "3" if h1 == "2" else "9"
        if m1 == "?":
            m1 = "5"
        if m2 == "?":
            m2 = "9"
        rst = "{}{}:{}{}".format(h1, h2, m1, m2)
        return rst
