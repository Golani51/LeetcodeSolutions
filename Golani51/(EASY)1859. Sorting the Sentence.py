class Solution:
    def sortSentence(self, s: str) -> str:
        myList = s.split()
        # print(myList[1][-1:])
        myStr = [0] * (len(myList))
        for i in range(len(myList)):
            index = int(myList[i][-1])
            if myList[i][-1].isdigit():
                # print("this is i:", i)
                # print("This is starting Index:", index)
                newWord = myList[i]
                # print("This is newWord after setting it equal to the ith word in myList:", newWord)
                newWord = newWord[:-1]
                # print("This is newWord after slicing the number off it:", newWord)
                # myList[index - 1] = newWord
                # print("This is myList[index-1]:",myList[index - 1])
                # myStr.insert(index - 1,newWord)
                myStr[index - 1] = newWord
                # print("This is the answer array:", myStr)
                # print("this is the original array:",myList)
                # print(newWord)
        return " ".join(myStr)
        # print(myStr)
