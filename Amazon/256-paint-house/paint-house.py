class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        dp = [0,0,0]

        for i in range(len(costs)):
            dp0 = costs[i][0] + min(dp[1], dp[2]) 
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[0], dp[1])

            dp = [dp0, dp1, dp2]

        return min(dp)


        # def paint_cost(n, color):
        #     total_cost = costs[n][color]

        #     if n == len(costs) - 1:
        #         return total_cost
            
        #     if color == 0:
        #         total_cost += min(paint_cost(n+1, 1), paint_cost(n+1, 2))
        #     elif color == 1:
        #         total_cost += min(paint_cost(n+1,0), paint_cost(n+1, 2))
        #     else:
        #         total_cost += min(paint_cost(n+1, 0), paint_cost(n+1, 1))

        #     return total_cost

        # if not costs:
        #     return 0
        # return min(paint_cost(0,0), paint_cost(0,1), paint_cost(0,2))



# TC = O(2^n) bcoz for every house we have two options
# SC = O(n) for runtime stack

