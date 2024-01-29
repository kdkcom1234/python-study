def createStr(values: list[int, str]):
  result = ""
  for val in values:
    result += str(val)
  return result

print(createStr(["h", "e", 1, 1, 0]))