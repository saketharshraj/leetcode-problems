# https://leetcode.com/problems/count-integers-in-intervals/submissions/

class CountIntervals:

    def __init__(self):
        self.data = []
        self.rangeCount = 0

    def add(self, left: int, right: int) -> None:
        old_range, new_range = None, None
        for i in range(len(self.data)):
            if new_range:
                break
            interval = self.data[i]
            lower, upper = interval[0], interval[1]
            old_range = [lower, upper]
            if left < lower and right > upper:
                self.data[i][0] = left
                self.data[i][1] = right
                new_range = [left, right]
            elif left < lower and lower <= right <= upper:
                self.data[i][0] = left
                new_range = [left, upper]
            elif lower <= left <= upper and right > upper:
                self.data[i][1] = right
                new_range = [lower, right]
            elif left >= lower and right <= upper:
                new_range = 1  # no need change anything in data
        if not new_range:
            self.data.append([left, right])
            self.rangeCount += right - left + 1
            return None
        
        old = old_range[1] - old_range[0] + 1
        new = new_range[1] - new_range[0] + 1
        self.rangeCount += new - old
        
    def count(self) -> int:
        return self.rangeCount


# Your CountIntervals object will be instantiated and called as such:
obj = CountIntervals()
obj.count()
obj.add(8, 43)
print(obj.data)
obj.add(13, 16)
print(obj.data)
obj.add(26, 33)
print(obj.data)
obj.add(28, 36)
print(obj.data)
obj.add(29, 37)
print(obj.data)
ans = obj.count()
print(ans)