Question: (first bad version)
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
		# here we can use binary search method
        l = 1  # initalised to 1
        r = n  # initalised to n
        while l < r:  # as long as it satifies
            m = (l + r) / 2  # finding the mid
            if isBadVersion(m):  
			# if the mid is bad, then we got the bad item, 
			# can go on search for previous, so m is replaces as r and can be search from l to r(which is m now)
			# we repeat it in while loop
                r = m
            else:
			# if not, these mean there no bad in (l to mid)
			# how can we justify it? question itself speaks that.
                l = m + 1
        return l
                    