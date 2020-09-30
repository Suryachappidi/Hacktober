class Solution(object):
  def twoSum(self, nums, target):
    print("The sum of two will be")
    d = {}
    for i, num in enumerate(nums):
      if target - num in d:
        return [d[target - num], i]
      d[num] = i
