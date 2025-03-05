class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_idx = 0
        word_idx = 0

        while abbr_idx < len(abbr) and word_idx < len(word):
            # If it's a digit, process number
            if abbr[abbr_idx].isdigit():
                if abbr[abbr_idx] == '0':  # Leading zeros are invalid
                    return False
                
                count_word = ''
                while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
                    count_word += abbr[abbr_idx]
                    abbr_idx += 1
                
                word_idx += int(count_word)  # Skip characters in word

            else:  # Match letters
                if word[word_idx] != abbr[abbr_idx]:  # Mismatch
                    return False
                
                word_idx += 1
                abbr_idx += 1

        return word_idx == len(word) and abbr_idx == len(abbr)
