class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index_number_map: dict = {}

        for index, num in enumerate(nums):
            complement: int = target - num
            print(index_number_map)
            if complement  in index_number_map:
                return [index, index_number_map[complement]]
            else:
                index_number_map[num] = index
        return []


