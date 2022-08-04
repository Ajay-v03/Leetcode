'''An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.
 
 Input: s = "anagram", t = "nagaram"
Output: true    '''

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == '__main__':
    root = Solution()
    s,t = "anagram","nagaram"
    print(root.isAnagram(s,t))