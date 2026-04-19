class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        currMin = nums[0]
        # Note that after rotating, it creates 2 sorted sequences separated by a inflection point
        # The sequence on the right is always larger than the left sequence
        while low <= high:
            mid = (low + high) // 2
            currMin = min(currMin, nums[mid])

            if nums[low] < nums[high]:
                # This means the entire sequence is sorted
                currMin = min(currMin, nums[low])
                return currMin
            else:
                # There is still an inflection point somewhere
                if nums[mid] >= nums[low]:
                    # mid and low are in the same sequence
                    # search to the right
                    low = mid + 1
                else:
                    # low is in the right sequence, mid is in the left sequence
                    # search to the left
                    high = mid - 1
        return currMin
            


