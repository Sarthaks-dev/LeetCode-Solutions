class Solution:
    def sortString(self,s):
        s1 = list(s)
        s1.sort()
        return "".join(s1)
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = {}
        for s in strs:
            key = self.sortString(s)
            print(key)
            if key in dict:
                dict[key].append(s)
            else:
                dict[key] = [s]
        return list(dict.values())