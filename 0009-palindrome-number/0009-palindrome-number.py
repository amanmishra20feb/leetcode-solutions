class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = 0
        i = x

        while (i > 0):
            rev = (rev * 10) + i % 10
            i = i // 10
        if (x == rev):
            return True
        else:
            return False 
