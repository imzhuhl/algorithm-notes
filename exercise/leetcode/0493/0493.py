from typing import List

class Solution:
    """归并排序
    """
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0
        self.mergeSort(nums, 0, len(nums)-1)
        return self.cnt

    def mergeSort(self, nums, left, right):
        if left >= right:
            return 

        mid = (left + right) // 2
        
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid+1, right)

        # merge 前先做统计
        j = mid+1
        for i in range(left, mid+1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            self.cnt += j - (mid+1)

        # merge
        i = left
        j = mid+1
        tmp = [0 for _ in range(right+1-left)]
        idx = 0
        while idx < len(tmp):
            if i > mid:
                tmp[idx] = nums[j]
                j += 1
            elif j > right:
                tmp[idx] = nums[i]
                i += 1
            else:
                if nums[i] < nums[j]:
                    tmp[idx] = nums[i]
                    i += 1
                else:
                    tmp[idx] = nums[j]
                    j += 1
            idx += 1
        
        nums[left:right+1] = tmp


class Solution2:
    def reversePairs(self, nums: List[int]) -> int:
        pass
    

if __name__ == '__main__':
    nums = [2,4,3,5,1]
    sl = Solution()
    rst = sl.reversePairs(nums)
    print(nums)
    print(rst)