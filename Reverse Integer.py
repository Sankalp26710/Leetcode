class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        max_int=2**31 -1
        min_int=-2**31
        n=abs(x)
        t=0
        while(n>0):
            if max_int//10<t:
                return 0
            t=t*10+n%10
            n=n//10
        if(x<0):
            t=t*-1
        return t
            
        