class Solution(object):
  def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = maxlen = 0
        
        for i, c in enumerate(s):
            if c in d and start <= d[c]:
                start = d[c] + 1
            else:
                maxlen = max(maxlen, i-start + 1)
            d[c] = i 
        return maxlen
if __name__ == "__main__":
    ans = Solution()
    print (ans.lengthOfLongestSubstring("abrtaet"))
