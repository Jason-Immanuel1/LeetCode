"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Store the numbers in a dictionary
        numbers_dict = {}

        for number in nums:
            if number in numbers_dict:
                numbers_dict[number] += 1
            else:
                numbers_dict[number] = 1

        # Return the Key with the most frequent values
        return max(numbers_dict, key=numbers_dict.get)


solution = Solution()
print(solution.majorityElement([3,2,3,45]))
