class Solution:

    def encode(self, strs: List[str]) -> str:
        strs.insert(0, str(len(strs)))
        return "*/*".join(strs)
    def decode(self, s: str) -> List[str]:
        length, words = s.split("*/*")[0], s.split("*/*")[1:]
        if length == 0: return []
        return words
            