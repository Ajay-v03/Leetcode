'''Program to check if a string is palindrome or not.
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.'''

'''
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
from logging import root


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(val for val in s if s.isalnum()).lower()
        return s == s[::-1]


if __name__ == '__main__':
    root = Solution()
    s = "A man, a plan, a canal: Panama"
    print(root.isPalindrome(s))



        