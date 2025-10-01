class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicates: dict = {}
        for num in nums:
            if num in duplicates:
                return True
            else:
                duplicates[num] = 1
        return False