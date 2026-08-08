class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        total = 0

        if operations is None:
            return 0

        for s in operations:
            if s == "D":
                if len(scores) > 0:
                    scores.append(scores[-1]*2)
            elif s == "C":
                if len(scores) > 0:
                    scores.pop()
            elif s == "+":
                if len(scores) >= 2:
                    scores.append(scores[-2] + scores[-1])
            else:
                scores.append(int(s))

        for s in scores:
            total +=s

        return total
            

            