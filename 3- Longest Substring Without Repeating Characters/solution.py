def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    currentStr = 0
    maxLen = 0
    index = 0
    while True:
        if index >= len(s):
            return maxLen
        if (s[index] in charSet):
            temp = 0
            while s[index] in charSet:
                charSet.remove(s[index - currentStr + temp])
                temp += 1
            charSet.add(s[index])
            currentStr = len(charSet)
        else:
            charSet.add(s[index])
            currentStr += 1
            maxLen = max(maxLen, currentStr)
        index += 1


print(lengthOfLongestSubstring("anviaj"))
