class Solution:
    def generateHashKey(self, word):
        result = [0 for _ in range(25)]
        for char in word:
            alphabetIndex = ord(char) - ord('a')
            result[alphabetIndex] += 1
        return tuple(result)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for i in range(len(strs)):
            hashKey = self.generateHashKey(strs[i])
            if anagramMap.get(hashKey) != None:
                anagramMap[hashKey].append(i)
            else:
                anagramMap[hashKey] = [i]
        
        returnArr = []
        for value in anagramMap.values():
            currArr = []
            for i in value:
                currArr.append(strs[i])
            returnArr.append(currArr)
        return returnArr

            

