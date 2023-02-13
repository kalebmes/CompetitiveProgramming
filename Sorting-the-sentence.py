class Solution:
    def sortSentence(self, s: str) -> str:
        answer = ['' for word in s.split()]
        for wordnum in s.split():
            answer[int(wordnum[-1])-1] = wordnum[:-1]
        return ' '.join(answer)
