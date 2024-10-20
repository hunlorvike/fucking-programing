class Solution:
    def checkExist(self, array, target):
        for i in range(len(array)):
            if array[i] == target:
                return i
        return -1
