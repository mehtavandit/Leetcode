class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)

    # Step 2: BFS to find max inform time
        queue = deque([(headID, 0)])  # (employee, time taken so far)
        max_time = 0

        while queue:
            emp_id, time_taken = queue.popleft()
            max_time = max(max_time, time_taken)
            for sub in graph[emp_id]:
                queue.append((sub, time_taken + informTime[emp_id]))
            
        return max_time
        