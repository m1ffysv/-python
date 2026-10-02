class Solution(object):
  def wordBreak(self, s, wordDict):
    words = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
      for j in range(i):
        if dp[j] == True and s[j:i] in words:
          dp[i] = True
          break
    if dp[len(s)] == True:
      return True
    else:
      return False