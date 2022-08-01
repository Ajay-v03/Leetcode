'''A program to reverse a number in Python
input = 123
output = 321'''

import code

class Solution:
    def reverse_int(self,num):
        rev = 0
        while num > 0:
            rev = rev *10 + num %10
            num = num // 10
            
        return rev

if __name__ == '__main__':
    root = Solution()
    print(root.reverse_int(123))