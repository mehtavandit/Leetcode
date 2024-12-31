from collections import defaultdict

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dict_ = defaultdict(list)

        for num in arr:
            dict_[abs(num-x)].append(num)

        sorted_dict = sorted(dict_.keys())

        result = []

        for i in sorted_dict:
            for num in dict_[i]:
                result.append(num)
                
                if len(result) == k:
                    break

            if len(result) == k:
                break
        

        result.sort()
        return result