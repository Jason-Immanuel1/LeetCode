"""
912. Sort an Array

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
"""

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        #Base Case: Check if array has one element
        if len(nums) < 2:
            return nums

        middle = len(nums) // 2
        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])

        return self.merge(left, right)

    def merge(self, left, right):
        #Store the sorted subarray
        result = []
        # Left and right pointer
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            # Check if left value is greater than right value
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:#
                # Right value is greater than left value
                result.append(right[j])
                j += 1

        # Add the remaining elements
        result.extend(left[i:])
        result.extend(right[j:])

        return result

