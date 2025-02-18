"""
Given two strings containing backspaces (identified by character '#'), check if the two strings are equal.

Example 1:
Input: str1 = "xy#z", str2 = "xzz#"
Output: True
Explanation: After applying backspaces, the strings become "xz" respectively.

Example 2:
Input: str1 = "xy#z", str2 = "xyz#"
Output: False
Explanation: After applying backspaces, the strings become "xz" and "xy" respectively

Example 3:
Input: str1 = "xp#", str2 = "xyz##"
Output: True
Explanation: After applying backspaces, the strings become "x" and "x" respectively.
            In "xyz##", the first "#" removes the character "z" and the second "#" removes the character "y".
"""

# Naive approach

def compare_strings(str1, str2):
    hash_count1 = 0
    hash_count2 = 0
    word1 = list(str1)
    word2 = list(str2)

    for i in word1:
        if i == "#":
            hash_count1 += 1

    for j in word2:
        if j == "#":
            hash_count2 += 1

    while hash_count1 > 0:
        word1.pop(word1.index('#') - 1) # this removes the first char before the first '#'
        word1.pop(word1.index('#')) # this gets the first occurrence of '#' in the word
        hash_count1 -= 1

    while hash_count2 > 0:
        word2.pop(word2.index('#') - 1)
        word2.pop(word2.index('#'))
        hash_count2 -= 1

    return word1 == word2


print(compare_strings("xy#z", "xzzz##"))