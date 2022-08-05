'''Program to find longest consecutive elements sequence.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.'''

from logging import root
from turtle import left, right
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        result = 0

        for num in nums:
            if num - 1 not in nums:
                left = num
                right = num
                while right + 1 in nums:
                    right += 1
                
                result = max(result, right - left + 1)
        return result


if __name__ == '__main__':
    root = Solution()
    nums = [100,4,200,1,3,2]
    print(root.longestConsecutive(nums))