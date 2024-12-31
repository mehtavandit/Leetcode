from collections import defaultdict

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # dict_ = defaultdict(list)

        # for num in arr:
        #     dict_[abs(num-x)].append(num)

        # sorted_dict = sorted(dict_.keys())

        # result = []

        # for i in sorted_dict:
        #     for num in dict_[i]:
        #         result.append(num)
                
        #         if len(result) == k:
        #             break

        #     if len(result) == k:
        #         break
        

        # result.sort()
        # return result

        idx = 0
        n = len(arr)

        for i in range(n-1, 0, -1):
            if (arr[i] <= x):
                idx = i
                break

        left, right = idx, idx+1
        result = []
        for _ in range(k):
            if left>=0 and right< len(arr):
                if abs(arr[left] - x) <= abs(arr[right]-x):
                    result.append(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            elif left>=0:
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right+=1

        return sorted(result)