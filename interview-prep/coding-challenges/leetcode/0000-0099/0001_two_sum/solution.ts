function twoSum(nums: number[], target: number): number[] {
  const numDic: { [key: number]: number } = {}; // Dictionary to store the number and its index
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const complement = target - num;
    if (complement in numDic) {
      // Check if the complement exists in the dictionary
      return [numDic[complement], i]; // Return indices if complement is found
    }
    numDic[num] = i; // Store the current number as the key and index as the value
  }
  return []; // Return an empty array if no solution is found
}
