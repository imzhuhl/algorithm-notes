from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        first_list = []
        second_list = []  # item number >= 3

        for item in nums:
            flag = False
            for i in range(len(first_list)):
                fl = first_list[i]
                if fl[0] + 1 == item:
                    flag = True
                    fl[0] = item
                    fl[1] += 1
                    if fl[1] == 3:
                        second_list.append(fl)
                        del first_list[i]
                    break
            if flag: continue
            for i in range(len(second_list)):
                sl = second_list[i]
                if sl[0] + 1 == item:
                    flag = True
                    sl[0] = item
                    sl[1] += 1
                    break
            if flag: continue
            n_lst = [item, 1]
            first_list.append(n_lst)
        
        if len(first_list) == 0:
            return True

        return False
                

if __name__ == '__main__':
    print(Solution().isPossible([1,2,3,4,4,5]))
            