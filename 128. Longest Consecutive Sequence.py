"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        number_set = set(nums)
        number_map = {}

        for number in nums:
            if number in number_map:
                number_map[number] += 1
            else:
                number_map[number] = 1



sol = Solution()
print(sol.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))