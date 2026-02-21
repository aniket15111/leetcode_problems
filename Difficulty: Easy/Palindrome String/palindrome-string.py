class Solution:
    def isPalindrome(self, s):
        new=s[::-1]
        if(new==s):
            return True
        else:
            return False
