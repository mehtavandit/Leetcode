from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # invalid = set()
        # transaction_map = defaultdict(list)
        
        # # Step 1: Parse transactions and store them in a structured format
        # parsed = []
        # for t in transactions:
        #     name, time, amount, city = t.split(',')
        #     time, amount = int(time), int(amount)
        #     parsed.append((name, time, amount, city, t))
        #     transaction_map[name].append((time, amount, city, t))

        # print(transaction_map)
        
        # # Step 2: Check conditions for invalid transactions
        # for name, records in transaction_map.items():
        #     # ✅ Sort by time to simplify comparison
        #     records.sort(key=lambda x: x[0])
            
        #     for i in range(len(records)):
        #         t1, amount1, city1, original_t1 = records[i]
                
        #         # ✅ Condition 1: Amount exceeds 1000
        #         if amount1 > 1000:
        #             invalid.add(original_t1)
                
        #         # ✅ Condition 2: Within 60 minutes + different city
        #         for j in range(i + 1, len(records)):
        #             t2, amount2, city2, original_t2 = records[j]
                    
        #             # If time difference exceeds 60, stop further checking (since sorted by time)
        #             if t2 - t1 > 60:
        #                 break
                    
        #             if city1 != city2:
        #                 invalid.add(original_t1)
        #                 invalid.add(original_t2)
        
        # # Step 3: Return invalid transactions as a list
        # return list(invalid)

        d = defaultdict(list)  # Mapping of names to their transaction details.
        idx = set()  # Set of indices of possibly invalid transactions.

        for i, x in enumerate(transactions):
            name, time, amount, city = x.split(",")
            time, amount = int(time), int(amount)
            d[name].append((time, city, i))
          
            # Check if the transaction amount exceeds $1000.
            if amount > 1000:
                idx.add(i)
              
            # Check for transactions with the same name in different cities within 60 minutes.
            for t, c, j in d[name]:
                if c != city and abs(time - t) <= 60:
                    idx.add(i)
                    idx.add(j)

        # Generate a list of transactions that are possibly invalid.
        return [transactions[i] for i in idx]
