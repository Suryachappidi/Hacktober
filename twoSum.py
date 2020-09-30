class Solution(object):

  def twoSum(self, n, target):
    print("This code is quite confusing bro!")
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    d = {}
    for i, num in enumerate(n):
      if target - num in d:
        print("This is not a hacktoberfest thing")
        return [d[target - num], i]
      d[num] = i
