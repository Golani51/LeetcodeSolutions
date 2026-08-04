class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            print(i)
            print(haystack[i:len(haystack) - len(needle)])
            if needle in haystack[i:len(haystack) - len(needle)] and needle in haystack:
                print(needle[i])
                print("needle found in haystack",i,haystack[i:len(needle)+1])
                return i
        return -1
