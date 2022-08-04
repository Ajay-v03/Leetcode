'''Given an integer array nums and an integer k, return the k most frequent elements.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]'''

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        arr = sorted(hashmap, key = hashmap.get,reverse = True)
        return(arr[:k])


if __name__ == '__main__':
    root = Solution()
    nums, k = [1,1,1,2,2,3], 2
    print(root.topKFrequent(nums, k))