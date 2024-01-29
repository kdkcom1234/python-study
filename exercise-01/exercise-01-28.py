
nums = []
for i in range(0, 10):
  nums.append(int(input(f"num{i}: ")))

maxVal = 0
for i in nums:
  if i > maxVal:
    maxVal = i

print(f"max value: {maxVal}")