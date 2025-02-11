class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            length = min(len(word1), len(word2))

            for j in range(length):
                if word1[j] != word2[j]:
                    if order.index(word1[j]) < order.index(word2[j]):
                        break
                    else:
                        return False

            else:
                # If we finished the loop and one word is a prefix of the other,
                # we need to check that word1 should be shorter than word2.
                if len(word1) > len(word2):
                    return False
                
        return True
                