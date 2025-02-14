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

