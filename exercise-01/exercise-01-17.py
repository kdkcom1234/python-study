def calcFactorial(val: int):
  result = 1
  for i in range(2, val + 1):
    result *= i
  return result

print(calcFactorial(5))
print(calcFactorial(10))

