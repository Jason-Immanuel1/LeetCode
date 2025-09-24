"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Check if the list only has one element
        if len(strs) < 2:
            return [strs]

        # Store the anagrams
        anagrams_list = {}

        for word in strs:
            # Sort the word
            key = "".join(sorted(word))
            # Check if the key is in the dictionary
            if key not in anagrams_list:
                anagrams_list[key] = []
            # Add the word to the list
            anagrams_list[key].append(word)

        return list(anagrams_list.values())