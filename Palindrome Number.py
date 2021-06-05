class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        t=0
        n=x
        while (n>0):
            t=t*10+n%10
            n=n//10
        if(t==x):
            return True
        else:
            return False