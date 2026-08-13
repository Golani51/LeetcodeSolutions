class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # indexSum = 0
        # # at the start we dont know if there are any solutions
        # # index sum will never be -1
        # # -1 is a sentinel value ( value that has some special meaning)
        # bestIndexSum = len(list1) + len(list2)
        # ans = []
        # for i in range(len(list1)):
        #     for j in range(len(list2)):
        #         if list1[i] == list2[j]:
        #             print(i, j, list1[i], list2[j])
        #             # add the indices of the words that match
        #             # keep that and compare it to any other words that match
        #             indexSum = i + j
        #             print(indexSum, bestIndexSum)
        #             if indexSum == bestIndexSum:
        #                 if list1[i] not in ans:
        #                     ans.append(list1[i])
        #             elif indexSum < bestIndexSum:
        #                 bestIndexSum = indexSum
        #                 ans = [list1[i]]
        #                 print(bestIndexSum)
        # if len(ans) == 0:
        #     ans.append(list1[0])
        # return ans
        ans = []
        maxKIndex = (len(list1) + len(list2))-2
        # k will now be inclusive
        for k in range(maxKIndex + 1):
            # i is inclusive because it goes up to and including k
            # 0 to k inclusive
            # These two con ditions turn into our max range for i
            # i < len(list1)
            # i < k + 1
            for i in range(max(k-len(list2) + 1,0), min(len(list1),k+1)):
                # if i <= k - len(list2):
                # continue
                j = (k - i)
                # print("i,j,k",i,j,k)
                # do the words match
                # append them
                if list1[i] == list2[j]:
                    ans.append(list1[i])
            if len(ans) > 0:
                return ans
        return []
