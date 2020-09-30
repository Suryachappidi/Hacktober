class Solution(object):
  def twoSum(self, n, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, num in enumerate(n):
      if target - num in d:
        return [d[target - num], i]
      d[num] = i
