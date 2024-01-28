class Solution:
    def findWordsContaining(self, words, x):
        output = []
        index = 0
        for word in words:
            index += 1
            set_word = set(word)
            for letter in set_word:
                if letter == x:
                    output.append(index-1)

        return print(output)
    
obj = Solution()
obj.findWordsContaining(["leet","code"], 'e')
obj.findWordsContaining(["abc","bcd","aaaa","cbc"], 'a')
obj.findWordsContaining(["abc","bcd","aaaa","cbc"], 'z')