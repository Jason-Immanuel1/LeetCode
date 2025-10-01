class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) < 2:
            return [strs]

        anagram_map: dict[str, list] = {}

        for index, word in enumerate(strs):
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_map:
                anagram_map[sorted_word].append(word)
            else:
                anagram_map[sorted_word] = [word]

        return list(anagram_map.values())