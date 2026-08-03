class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        count = 0
        lis = []
        i=0
        while i < len(s)-1:
            j = i
            while s[j] != "#":
                j+=1
                
            count = int(s[i:j])
            print(count)
            start = j + 1
            end = start + count
            lis.append(s[j+1:end])
            i = end
        return lis