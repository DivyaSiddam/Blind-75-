#https://www.designgurus.io/viewer/document/grokking-the-coding-interview/636b1d083b22faa3e89b2458
class Solution:
    def findMaxSumSubArray(self, k, arr):
        n = len(arr)
        max_sum = 0

        for i in range(n - k + 1):
            total = 0
            for j in range(i, i + k):
                total += arr[j]
            if total > max_sum:
                max_sum = total

        return max_sum
