class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(0, len(nums)):
            # Check if the complement of current number is in map
            if myMap.get(nums[i]) != None:
                return [myMap.get(nums[i]), i]
            complement = target-nums[i]
            myMap[complement] = i
