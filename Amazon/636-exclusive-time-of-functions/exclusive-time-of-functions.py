class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        previous_time = 0

        for log in logs:
            func_id, action, timestamp = log.split(":")
            func_id, timestamp = int(func_id), int(timestamp)

            if action == "start":
                if stack:
                    result[stack[-1]] += timestamp - previous_time
                stack.append(func_id)
                previous_time = timestamp
            else:
                result[stack.pop()] += timestamp - previous_time + 1
                previous_time = timestamp + 1

        return result