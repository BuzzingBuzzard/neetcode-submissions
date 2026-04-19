class Solution:

    def encode(self, strs: List[str]) -> str:
        lenArr = []
        for string in strs:
            lenArr.append(len(string))
        returnStr = ''
        for i in range(len(strs)):
            returnStr += (str(lenArr[i]) + "#" + strs[i])

        return returnStr

    def decode(self, s: str) -> List[str]:
        currStr = s
        returnArr = []
        pointer = 0
        while True:
            delimiterIndex = currStr.find("#")
            if delimiterIndex == -1:
                break
            currLen = int(currStr[0 : delimiterIndex])
            strStart = delimiterIndex + 1
            strEndPlusOne = strStart + currLen
            returnArr.append(currStr[ strStart : strEndPlusOne ])
            if strEndPlusOne < len(currStr):
                currStr = currStr[strEndPlusOne : len(currStr)]
            else:
                break
        return returnArr

