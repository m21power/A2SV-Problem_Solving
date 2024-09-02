# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        count = 0
        for i,ch in enumerate(word):
            if ch in 'aeiuo':
                count += (i + 1) * (n - i)
        return count