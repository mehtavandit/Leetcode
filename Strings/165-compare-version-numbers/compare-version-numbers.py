class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split(".")
        l2 = version2.split(".")
        
        max_len = max(len(l1), len(l2))
        
        for i in range(max_len):
            num1 = int(l1[i]) if i < len(l1) else 0
            num2 = int(l2[i]) if i < len(l2) else 0
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        # If all revisions are equal
        return 0