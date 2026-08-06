class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = {}
        window = {}
        left = 0

        for char in s1:
            target[char] = target.get(char, 0) + 1

        for right in range(len(s2)):
            char_right = s2[right]
            window[char_right] = window.get(char_right, 0) + 1

            if right-left+1 > len(s1):
                char_left = s2[left]
                window[char_left] -= 1

                if window[char_left] == 0:
                    del window[char_left]

                left += 1

            if window == target:
                return True
        return False