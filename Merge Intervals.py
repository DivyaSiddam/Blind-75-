# https://www.designgurus.io/viewer/document/grokking-the-coding-interview/63923e6de4cb724ea719007a
class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        # Sort based on start time
        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]

        for current in intervals[1:]:
            last = result[-1]
            if current.start <= last.end:
                last.end = max(last.end, current.end)
            else:
                result.append(current)

        return result
