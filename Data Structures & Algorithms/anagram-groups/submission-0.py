class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for s in strs:
            sortedkey = "".join(sorted(s))
            if sortedkey not in hashtable:
                hashtable[sortedkey] = []
            hashtable[sortedkey].append(s)

        result = []
        for value in hashtable.values():
            result.append(value)

        return result