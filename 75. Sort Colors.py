"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(1, len(nums)):
            current = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > current:
                nums[j +1] = nums[j]
                j -= 1
            nums[j+1] = current
