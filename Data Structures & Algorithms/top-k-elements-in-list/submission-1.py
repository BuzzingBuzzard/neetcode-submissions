import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        priority_queue = []
        for element, freq in freqMap.items():
            heapq.heappush(priority_queue, (freq, element))
            if len(priority_queue) > k:
                heapq.heappop(priority_queue)
        returnArr = []
        for i in range(k):
            returnArr.append(heapq.heappop(priority_queue)[1])
        return returnArr
        