# https://www.designgurus.io/viewer/document/grokking-the-coding-interview/63d93a25970f20b6d90eef04
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
