from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        
        state = [0 for _ in range(len(ratings))]
        state[0] = 1 if ratings[0] <= ratings[1] else -1
        state[-1] = 1 if ratings[-1] <= ratings[-2] else -1
        
        for i in range(1, len(ratings)-1):
            if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                state[i] = 1
                continue
            
            if ratings[i] >= ratings[i-1] and ratings[i] >= ratings[i+1]:
                state[i] = -1

        print(state)
        flag = False
        for i in range(len(ratings)):
            if state[i] == 1:
                flag = True
            elif state[i] == -1:
                flag = False
            else:
                if flag:
                    state[i] = state[i-1] + 1
        print(state)

        for i in range(len(ratings)-1, -1, -1):
            if state[i] == 1: flag = True
            elif state[i] == -1: flag = False
            else:
                if flag:
                    state[i] = state[i+1] + 1
        print(state)
                    
        if state[0] == -1:
            state[0] = state[1] + 1
        if state[-1] == -1:
            state[-1] = state[-2] + 1
        cnt = state[0] + state[-1]
        for i in range(1, len(ratings)-1):
            if state[i] == -1:
                if state[i-1] == -1:
                    cnt += state[i+1] + 1
                elif state[i+1] == -1:
                    cnt += state[i-1] + 1
                else:
                    cnt += max(state[i-1], state[i+1]) + 1
            else:
                cnt += state[i]
        return cnt


class Solution2:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in range(len(ratings))]

        for i in range(1, len(candies)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        # print(candies)

        for i in range(len(candies)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
        # print(candies)

        return sum(candies)



if __name__ == '__main__':
    # ratings = [1, 2, 2, 2, 1, 2, 3, 4, 3, 2, 1, 4, 5]
    ratings = [29,51,87,87,72,12]
    sl = Solution2()
    ret = sl.candy(ratings)
    print(ret)

