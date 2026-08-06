class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""

        for s in strs:
            ret += str(len(s)) + "#" + s

        return ret  

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j+=1

            l = int(s[i:j])

            start = j+1
            end = start+l

            ret.append(s[start:end])

            i = end

        return ret


            