class Solution:
    def findMaximum(self, array):
        max_value = array[0]
        for i in range(len(array)):
            if array[i] > max_value:
                max_value = array[i]
        return max_value
