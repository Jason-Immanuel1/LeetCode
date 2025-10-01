class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        number_map: dict = {}
        i: int = 0
        result: list = []
        for num in nums:
            if num in number_map:
                number_map[num] += 1
            else:
                number_map[num] = 1


        while i < k:
            most_frequent = max(number_map, key=number_map.get)
            number_map.pop(most_frequent)
            result.append(most_frequent)
            i +=1
        return result
