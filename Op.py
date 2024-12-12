class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = len(nums)

        for i in range(a - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0

        result = [b for b in nums if b != 0]
        result = result + [0]* (a - len(result))   

        return result             
