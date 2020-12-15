class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]  # (n+1, m+1)

        for i in range(m+1):
            dp[0][i] = i
        
        for i in range(n+1):
            dp[i][0] = i

        for row in range(1, n+1):
            for col in range(1, m+1):
                tmp = dp[row-1][col-1] + 1
                if word1[col-1] == word2[row-1]:
                    tmp -= 1
                dp[row][col] = min(
                    tmp,
                    dp[row][col-1] + 1,
                    dp[row-1][col] + 1
                )
        return dp[-1][-1]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))
