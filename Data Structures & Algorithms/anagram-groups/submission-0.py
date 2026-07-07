from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result={}
        for i in strs:
            a="".join(sorted(i))
            if a in result:
                result[a].append(i)
            else:
                result[a]=[i]
        return list(result.values())