class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        empty_bottles = 0
        full_bottles = numBottles

        while full_bottles > 0:
            count += full_bottles
            empty_bottles += full_bottles
            full_bottles = 0

            new_full, empty_bottles = divmod(empty_bottles, numExchange)
            full_bottles += new_full

        return count