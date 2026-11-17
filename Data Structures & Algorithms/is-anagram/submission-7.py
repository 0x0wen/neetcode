class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashs = {}
        hasht = {}
        for c in s:
            if c not in hashs:
                hashs[c] = 1
            else:
                hashs[c] += 1
        for c in t:
            if c not in hasht:
                hasht[c] = 1
            else:
                hasht[c] += 1
        for key, val in hashs.items():
            if key not in hasht or hasht[key] != val:
                return False
        return True
