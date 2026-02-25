
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        keys = defaultdict(list)

        for num in arr:
            counts = bin(num).count('1')
            keys[counts].append(num)

        for k in keys:
            keys[k].sort()

        result = []

        for k in sorted(keys.keys()):
            result.extend(keys[k])

        return result






    