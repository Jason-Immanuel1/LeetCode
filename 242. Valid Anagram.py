"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the string are different
        if len(s) != len(t):
            return False

        # Count the amount of each letters
        letter_count = {}

        # Add the letters from s to the dictionary
        for letter in s:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        # Remove the letters from t from the dictionary
        for letter in t:
            if letter in letter_count:
                letter_count[letter] -= 1
            else:
                letter_count[letter] = 1

        # Check if there are any remaining letters in the dictionary
        for value in letter_count.values():
            if value != 0:
                return False

        return True







