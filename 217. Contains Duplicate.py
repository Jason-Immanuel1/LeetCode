"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        # Create a dictionary to store the seen numbers
        seen = {}

        for num in nums:
            if num in seen:
                # Return True if the number is already in the dictionary
                return True
            else:
                # Add numbers to the dictionary
                seen[num] = 1
        return False


