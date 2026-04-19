class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
 
        while l < r:
            curr_area = (r - l) * min(heights[l], heights[r])
            if curr_area > max_area:
                max_area = curr_area
            # Shift the pointer that has a smaller height
            # Since the area is limited by the min height
            # If both are equal (say H), shifting either is fine
            # Sicne a future height will be compared against H, and min(H, future height) will be updated again
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
    
        