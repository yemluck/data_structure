"""
 LeetCode 383:

 Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


# My naive solution
def can_construct(ransom_note, magazine):
    seen = {}

    for char in magazine:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1

    for char in ransom_note:
        if char not in seen:
            return False
        if seen[char] <= 0:
            return False
        else:
            seen[char] -= 1
    # If it runs through the whole for loop, return true
    return True


print(can_construct("a", "b"))
print(can_construct("aa", "ab"))
print(can_construct("aa", "aab"))
