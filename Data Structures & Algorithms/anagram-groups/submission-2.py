class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lis = []
        temp = {}
        for s in strs:
            temlis = [0] * 27
            for c in s:
                temlis[ord(c) - 96] += 1
            
            temp.setdefault(tuple(temlis), []).append(s)
            
        for key in temp:
            lis.append(temp[key])
        return lis
