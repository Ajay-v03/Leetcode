'''Reverse all words in a sentence without inbuilt function in Python'''

'''input = 'I love to play Football'
   output = 'Football play to love I'''
import re
class Solution:
    def word_reverser(self, sentence):
        
        words = re.findall(r'\w+', sentence)
        
        first = 0
        last = len(words)-1
        
        while (first <= last):
            
            temp = words[first]
            words[first] = words[last]
            words[last] = temp
            
            first += 1
            last -= 1
            
        
        result = ''
        for word in words:
            '''if word in result is '':
                result += word
            else:'''
            result += ' ' + word
                
        return result

if __name__ == '__main__':
    root = Solution()
    sentence = 'I love to play Football'
    print(root.word_reverser(sentence))




'''Reverse all words in a sentence with inbuilt function in Python'''

def word_reverser(sentence):
    
    if len(sentence) == 0:
        return sentence
    result = ' '.join(reversed(sentence.split()))
    return result

sentence = 'I love to play Football'
word_reverser(sentence)