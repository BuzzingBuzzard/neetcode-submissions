class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr_set = set()
        longest_len = 0
        for num in nums:
            arr_set.add(num)
        for num in arr_set: # Iterating in the set is more efficient than iterating the arr, since it has no duplicates
            if num - 1 in arr_set:
                # Number is not the start of a sequence
                continue
            else:
                # Number is the start of a sequence
                curr_seq_len = 0
                curr_number = num
                # Check how far can we increment the current number within arr_set
                while curr_number in arr_set:
                    curr_seq_len += 1
                    curr_number += 1
                if curr_seq_len > longest_len:
                    longest_len = curr_seq_len
        return longest_len

