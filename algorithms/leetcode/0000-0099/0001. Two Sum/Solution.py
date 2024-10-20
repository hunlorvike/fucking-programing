from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic = {}  # Dictionary to store the number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if (
                complement in num_dic
            ):  # Check if the complement exists in the dictionary
                return [num_dic[complement], i]  # Return indices if complement is found
            num_dic[num] = (
                i  # Store the current number as the key and index as the value
            )
