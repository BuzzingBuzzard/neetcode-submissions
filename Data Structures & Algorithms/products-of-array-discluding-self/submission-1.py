class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        zeroCount = 0
        for num in nums:
            if num != 0:
                totalProduct = totalProduct * num
            else:
                zeroCount += 1
        returnArr = []
        if zeroCount > 1:
            return [0 for _ in range(len(nums))]
        else:
            for num in nums:
                if zeroCount == 0:
                    returnArr.append(int(totalProduct / num))
                else:
                    if num != 0:
                        returnArr.append(0)
                    else:
                        returnArr.append(totalProduct)
        return returnArr
        