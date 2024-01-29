def checkSign(num):
  if(num == 0):
    return "0"
  elif(num > 0):
    return "양수"
  elif(num < 0):
    return "음수"
  
print(checkSign(0))
print(checkSign(2))
print(checkSign(-1))