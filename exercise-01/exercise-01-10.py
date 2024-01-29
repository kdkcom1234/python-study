def checkPrime(val):
  if(val < 2): 
    return False
  if(val == 2): 
    return True
  
  for num in range(2, val):
    if val % num == 0:
      return False 
  return True

print(checkPrime(2))
print(checkPrime(1))
print(checkPrime(3))
print(checkPrime(4))
print(checkPrime(5))