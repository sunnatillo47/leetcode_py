class Solution:
    def reverseWords(self, s: str) -> str:
        s += ' '
        reverse_word = ''
        word = ''

        for n in s:
            if n != ' ':
                word += n
            else:
                reverse_word += f" {word[::-1]}"
                word = ''

        return reverse_word[1:]