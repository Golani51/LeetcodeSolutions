class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n1 = None
        n2 = None
        n3 = None
        for num in nums:
            if num == n1 or num == n2 or num == n3:
                continue
            if n1 is None or num > n1:
                n3 = n2
                n2 = n1
                n1 = num
            elif n2 is None or num > n2:
                n3 = n2
                n2 = num
            elif n3 is None or num > n3:
                n3 = num
        print("n1,n2,n3",n1,n2,n3)
        if n3 is None:
            return n1
        return n3
        # first answer
        # mySet = set(nums)
        # # print("myset",mySet)
        # myList = sorted(list(mySet))
        # # print("myList",myList)
        # if len(myList) < 3:
        #     return myList[-1]
        # return myList[-3]
