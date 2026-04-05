class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unionSet = defaultdict(int)
        size = defaultdict(int)

        for num in nums:
            unionSet[num] = num
            size[num] = 1
        
        def find(member):
            if member != unionSet[member]:
                unionSet[member] = find(unionSet[member])
            return unionSet[member]
        
        def union(member1, member2):
            rep1 = find(member1)
            rep2 = find(member2)

            if rep1 == rep2:
                return

            if size[rep1] > size[rep2]:
                unionSet[rep2] = rep1
                size[rep1] += size[rep2]
            else:
                unionSet[rep1] = rep2
                size[rep2] += size[rep1]
        
        for key in unionSet:
            numberBefore = key - 1
            numberAfter = key + 1
            if numberAfter in unionSet:
                union(key, numberAfter)
            if numberBefore in unionSet:
                union(key, numberBefore)

        
        if len(size) > 0:
            return max(list(size.values()))
        else: return 0

