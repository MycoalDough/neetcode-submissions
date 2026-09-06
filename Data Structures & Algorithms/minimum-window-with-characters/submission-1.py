class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0 

        check = {}
        for i in t:
            check[i] = check.get(i, 0) + 1

        formed = 0
        req = len(check)
        curr = {}
        answer = ""

        while right < len(s):
            c = s[right]
            curr[c] = curr.get(c, 0) + 1
            if c in check and curr[c] == check[c]:
                formed += 1
            right += 1

            while formed == req:
                window = s[left:right]

                if answer == "" or len(answer) > len(window):
                    answer = window

                b = s[left]
                curr[b] -= 1
                if b in check and curr[b] < check[b]:
                    formed -= 1
                left += 1

        return answer