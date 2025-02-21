class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # count = defaultdict(int)

        # n = len(nums)

        # for i in range(n):
        #     count[nums[i]] += 1

        # for key in count:
        #     if count[key] %2 != 0 and count[key] %3!=0:
        #         return -1

        # main_operations = 0

        # for key in count:
        #     operation = 0
        #     while count[key] != 0:
        #         if count[key] % 3 == 0:
        #             count[key] -= 3
        #             operation += 1
                
        #         if count[key] %2 == 0:
        #             count[key] -= 2
        #             operation += 1

        #     main_operations += operation

        # return main_operations

        count = Counter(nums)

        operations = 0

        for values in (count.values()):
            if values == 1:
                return -1
            
            if values % 3 == 0:
                operations += values //3

            if values % 3 == 1:
                operations += (values // 3-1) + 2

            if values % 3 == 2:
                operations += values // 3 + 1

        return operations