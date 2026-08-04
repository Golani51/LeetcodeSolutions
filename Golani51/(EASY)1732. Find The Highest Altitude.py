class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        count = 0
        newAlt = 0
        for i in range(len(gain)):
            count += gain[i]
            print(count)
            if count > newAlt:
                newAlt = count
        return newAlt
