class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        i=2
        num=[0,1]
        while(i<=n):
            if(i%2==0):
                num+=[num[i//2]]
            else:
                num+=[num[(i//2)]+num[(i//2)+1]]
            i=i+1
        return max(num)