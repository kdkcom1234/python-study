num = int(input("num: "))

result = 0
for i in range(2, num+1, 2):
  result += i

# 10: 2 4 6 8 10 -> 5 * 12 / 2
print(result)