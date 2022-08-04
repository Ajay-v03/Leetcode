'''Program to check duplicates in a list

Input: nums = [1,2,3,1]
Output: true '''

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # return len(nums) > len(set(nums))
        list_ = len(nums)
        hashset_ = len(set(nums))
        
        return hashset_ < list_

if __name__ == '__main__':
    root = Solution()
    nums = [1,2,3,1]
    print(root.containsDuplicate(nums))