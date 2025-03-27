# https://www.designgurus.io/viewer/document/grokking-the-coding-interview/651534c6a869ec13cbff77d7
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
