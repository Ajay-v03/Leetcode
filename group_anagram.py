'''Given an array of strings strs, group the anagrams together.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]'''

from collections import defaultdict
from typing import List

# Without using python inbuilt functions
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for letter in strs:
            count = [0] * 26 #make a...z lowercase letters
            
            for char in letter:
                count[ord(char) - ord("a")] += 1
                
            hashmap[tuple(count)].append(letter)
            
        return hashmap.values()


# With using inbuilt functions
class Solution_1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for letter in strs:
            s = ''.join(sorted(letter))
            hashmap[s].append(letter)

        return hashmap.values()


if __name__ == '__main__':
    # root = Solution()
    root = Solution_1()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(root.groupAnagrams(strs))


