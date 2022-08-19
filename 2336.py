# https://leetcode.com/problems/smallest-number-in-infinite-set/
# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

# Implement the SmallestInfiniteSet class:

# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

import bisect

class SmallestInfiniteSet:

    def __init__(self):
        self.inf_set = [x for x in range(1,1001)]

    def popSmallest(self) -> int:
        return self.inf_set.pop(0)

    def addBack(self, num: int) -> None:
        if num in self.inf_set:
            return
        bisect.insort(self.inf_set,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
param_1 = obj.popSmallest()
param_1 = obj.popSmallest()
param_1 = obj.popSmallest()
obj.addBack(1)
obj.addBack(2)
param_1 = obj.popSmallest()
param_1 = obj.popSmallest()
print(param_1)
