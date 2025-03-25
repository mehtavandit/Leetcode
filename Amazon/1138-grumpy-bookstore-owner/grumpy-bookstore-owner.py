class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        unhappy_customers = 0

        for i in range(minutes):
            unhappy_customers += customers[i] * grumpy[i]

        maxunhappy_customers = unhappy_customers
        
        for i in range(minutes, n):
            unhappy_customers += customers[i] * grumpy[i]

            unhappy_customers -= customers[i-minutes] * grumpy[i-minutes]

            maxunhappy_customers = max(maxunhappy_customers, unhappy_customers)

        satisfied_customers = maxunhappy_customers

        for i in range(n):
            satisfied_customers += customers[i] * (1-grumpy[i])

        return satisfied_customers