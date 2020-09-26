from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.nums = nums
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == '__main__':
    k = 1
    arr = []
    kthlargest = KthLargest(k, arr)
    kthlargest.add(3)
    kthlargest.add(5)
    kthlargest.add(10)
    kthlargest.add(9)
    kthlargest.add(4)

