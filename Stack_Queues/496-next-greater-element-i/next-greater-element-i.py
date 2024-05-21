class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d={}
        n=len(nums2)
        for i in range(n):
            d[nums2[i]]=i
        a=[nums2[-1]]
        answer=[-1]
        for i in range(n-2,-1,-1):
            if a[-1]>nums2[i]:
                answer.append(a[-1])
            else:
                while len(a)>0:
                    if a[-1]>nums2[i]:
                        answer.append(a[-1])
                        break
                    else:
                        a.pop()
                if len(a)==0:
                    answer.append(-1)
            a.append(nums2[i])
        res=[]
        answer=answer[-1::-1]
        for i in nums1:
            res.append(answer[d[i]])
        return res


