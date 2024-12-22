class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        count = 0
        output = ""
        len1 = len(output)
        len2 = len(b)

        while(len1 <= len2):
            output = output + a
            count += 1
            len1 = len(output)

            result = b in output

            if(result):
                return count


        output += a
        count += 1
        
        # Check if b is now a substring
        if b in output:
            return count
        
        # If not found, return -1
        return -1