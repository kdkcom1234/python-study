def countChar(val: str, find: str):
  count = 0
  for char in val:
    if char == find:
      count = count + 1
  return count

print(countChar("hello", "l"))


