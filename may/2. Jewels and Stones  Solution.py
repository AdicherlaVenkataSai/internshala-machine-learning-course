Question:
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.

Hide Hint #1  
For each stone, check if it is a jewel.

solution:
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        jwel = {}  # empty dictionary
       
        for j in J:
            jwel[j] = 1  # for every character in J, we're assigning a key value as 1 to it in the created dict
        
        count = 0
        for s in S:
            if s in jwel:  # now for every char at S, we're checking if it matches with the one in dict
                count += 1  # if yes then we increase the count of the jwel found and return the count in end.
        return count
        
