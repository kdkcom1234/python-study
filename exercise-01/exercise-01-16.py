def countVowels(val: str):
  result = 0
  for c in ["a", "e", "i", "o", "u"]:
    result = result + val.lower().count(c)

  return result

print(countVowels("hello world"))