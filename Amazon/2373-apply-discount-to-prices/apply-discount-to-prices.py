class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(" ")

        for i in range(len(words)):
            word = words[i]
            if word[0] == "$" and word[1:].isdigit():
                price = word[1:]
                new_price = round(float(price) * (1 - discount / 100), 2)
                new_value = "$" + "{:.2f}".format(new_price)
                words[i] = new_value

        return ' '.join(words)