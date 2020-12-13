from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff_arr = [0 for _ in range(n)]

        for line in bookings:
            i, j, k = line[0]-1, line[1]-1, line[2]
            diff_arr[i] += k
            if j+1 < n:
                diff_arr[j+1] -= k
        
        # 复原数组
        for i in range(1, n):
            diff_arr[i] += diff_arr[i-1]
        
        return diff_arr


if __name__ == '__main__':
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    print(Solution().corpFlightBookings(bookings, n))
