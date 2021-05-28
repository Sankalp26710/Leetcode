<<<<<<< HEAD
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        neg_sum = -1
        if nums[-2] < 0:
            neg_sum = nums[0] * nums[-1] * nums[-2]
        poz_sum = nums[0] * nums[1] * nums[2]
=======
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        neg_sum = -1
        if nums[-2] < 0:
            neg_sum = nums[0] * nums[-1] * nums[-2]
        poz_sum = nums[0] * nums[1] * nums[2]
>>>>>>> 26eed3ecc0f857fc8585e21602a54525b57575db
        return neg_sum if neg_sum > poz_sum else poz_sum 