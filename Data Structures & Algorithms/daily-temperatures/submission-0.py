class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = [] # Stores pairs of (temperature, index)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, prev_idx = stack.pop()
                answer[prev_idx] = i - prev_idx
            stack.append((temp, i))
            
        return answer