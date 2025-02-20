from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        
        if endWord not in words:
            return 0

        q = deque()
        q.append((beginWord, 1))

        while q:
            word, level = q.popleft()

            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + char + word[i+1:]

                    if new_word == endWord:
                        return level + 1

                    if new_word in words:
                        words.remove(new_word)
                        q.append((new_word, level + 1))

        return 0