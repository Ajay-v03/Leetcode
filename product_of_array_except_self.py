'''product of array except nums[i] = product of numbers to the left of nums[i] * product of numbers to the right of nums[i]

Input: nums = [1,2,3,4]
Output: [24,12,8,6]'''

from logging import root
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in nums]
        
        left = 1
        right = 1
        
        for i in range(len(nums)):
            ans[i] *= left
            ans[~i] *= right
            left *= nums[i]
            right *= nums[~i]
        
        return ans
if __name__ == '__main__':
    root = Solution()
    nums = [1,2,3,4]
    print(root.productExceptSelf(nums))



