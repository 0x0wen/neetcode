class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = defaultdict(int)
        for n in nums:
            table[n] += 1
        
        return list(dict(sorted(table.items(), key=lambda item: item[1], reverse=True)))[:k]