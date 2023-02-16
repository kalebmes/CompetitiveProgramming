class Solution:
    def countVowels(self, word: str) -> int:
        res, prev = 0, 0
        for i in range(len(word)):
            c = word[i]
            if c in ['a', 'e', 'i', 'o', 'u']:
                prev += i + 1
            res += prev
        return res
