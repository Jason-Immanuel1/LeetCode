"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        number_count = {}

        for number in nums:
            if number in number_count:
                number_count[number] += 1
            else:
                number_count[number] = 1

        number_list = []

        for i in range(0, k):
            max_frequent = (max(number_count, key=number_count.get))
            number_list.append(max_frequent)
            number_count.pop(max_frequent)

        return number_list





