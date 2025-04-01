# https://www.designgurus.io/viewer/document/grokking-the-coding-interview/639f9a0cd239f7cde26dde2b
class Solution:
    def search(self, nums, key):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == key:
                return mid

            # Check if the left part is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= key < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right part must be sorted
            else:
                if nums[mid] < key <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
