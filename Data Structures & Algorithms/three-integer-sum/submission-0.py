class Solution:
    # For an array of nums, return the two values that adds up to the index
    def twoSum(self, nums, target):
        prevSet = set()
        returnArr = []
        for num in nums:
            diff = target - num
            if diff in prevSet:
                returnArr.append([num, diff])
            prevSet.add(num)
        return returnArr

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tripletSet = set()
        for i in range(len(nums)):
            # Solve the 2 sum problem for the subarray nums[i+1: len(nums)]
            twoSumArr = self.twoSum(nums[i+1: len(nums)], 0 - nums[i])
            if len(twoSumArr) > 0:
                for pair in twoSumArr:
                    triplet = pair + [nums[i]]
                    triplet.sort()
                    tripletSet.add(tuple(triplet))
        # Format the return
        returnArr = []
        for triplet in tripletSet:
            returnArr.append(list(triplet))
        return returnArr
        