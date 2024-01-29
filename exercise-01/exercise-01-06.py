def checkPalindrome(val : str):
  print(val)
  print(val[::-1])
  return val == val[::-1]

print(checkPalindrome("hello"))
print(checkPalindrome("level"))