'''Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].'''

from logging import root
from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num],index]
            else:
                dic[num] = index
                
if __name__ == '__main__':
    root = Solution()
    nums, target = [2,7,11,15], 9
    print(root.twoSum(nums,target))