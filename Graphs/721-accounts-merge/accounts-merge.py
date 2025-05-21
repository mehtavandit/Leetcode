from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return

        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        n = len(accounts)
        dsu = DSU(n)
        email_to_node = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_to_node:
                    email_to_node[email] = i
                else:
                    dsu.union(i, email_to_node[email])

        print(email_to_node)
        print(dsu.parent)


        merged_emails = defaultdict(list)
        for email, node in email_to_node.items():
            parent = dsu.find(node)
            merged_emails[parent].append(email)

        result = []
        for parent, emails in merged_emails.items():
            result.append([accounts[parent][0]] + sorted(emails))

        return result
