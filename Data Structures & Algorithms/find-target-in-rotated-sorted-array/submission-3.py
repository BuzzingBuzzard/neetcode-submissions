class Solution:
    def binarySearch(self, nums, left, right, target):
        low = left
        high = right
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        # Use lower bond to find the pivot first
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                # Pivot is to the right of mid
                low = mid + 1
            else:
                high = mid
        
        pivot = low

        print("pivot", pivot)

        # Use normal binary search on both halves
        left_search_result = self.binarySearch(nums, 0, pivot, target)
        if left_search_result != -1:
            return left_search_result
        return self.binarySearch(nums, pivot, len(nums)-1, target)



