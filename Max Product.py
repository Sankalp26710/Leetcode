class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        neg_sum = -1
        if nums[-2] < 0:
            neg_sum = nums[0] * nums[-1] * nums[-2]
        poz_sum = nums[0] * nums[1] * nums[2]
        return neg_sum if neg_sum > poz_sum else poz_sum 