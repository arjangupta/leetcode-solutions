# https://leetcode.com/problems/reverse-words-in-a-string/
# Solved date: 2023-08-23


class Solution:
    def reverseWords(self, s: str) -> str:
        words_arr = s.split(' ')
        words_arr.reverse()
        reduced_arr = []
        for word in words_arr:
            new_word = ''
            for c in word:
                if c != ' ':
                    new_word += c
            if new_word != '':
                reduced_arr.append(new_word)
        # print(reduced_arr)
        ans = ' '.join(reduced_arr)
        return ans