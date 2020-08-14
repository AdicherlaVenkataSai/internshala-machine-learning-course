Question:
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

 

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
You may assume that both strings contain only lowercase letters.

Solution:
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in ransomNote:  # for every alphabet in ransomNote
            if i in magazine:  # if it's in magazine, if all then we can create ransomNote
                magazine = magazine.replace(i, '', 1)  # were checking with replacing it, then it validates that it has all the alphabets to create ransomeNote
            else:
                return False  
        return True
        
