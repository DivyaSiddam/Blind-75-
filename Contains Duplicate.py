# https://www.designgurus.io/viewer/document/grokking-the-coding-interview/63d8efe7f8694f3655d60712
class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
