class Solution(object):
    def sumOfGoodNumbers(self, nums, k):

        total = 0

        for i in range(len(nums)):

            left = True
            right = True

            if i - k >= 0:
                if nums[i] <= nums[i - k]:
                    left = False

            if i + k < len(nums):
                if nums[i] <= nums[i + k]:
                    right = False

            if left and right:
                total = total + nums[i]

        return total
            

            




            