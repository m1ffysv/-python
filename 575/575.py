class Solution(object):
  def distributeCandies(self, candyType):
    unique_candies = set()
    for candy in candyType:
      unique_candies.add(candy)
    limit = len(candyType) // 2
    if len(unique_candies) > limit:
      return limit
    else:
      return len(unique_candies)