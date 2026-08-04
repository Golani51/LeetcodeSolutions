class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # TODO optimize
        count = 0
        maxCount = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                count = 0
            else:
                count += 1
                temp = count
                if temp > maxCount:
                    maxCount = temp
                #print("returning maxCount" , maxCount)
        #print(maxCount)
        return maxCount
