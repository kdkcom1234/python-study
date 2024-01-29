numbers = [1,2,3,4,5,6,7,8,9,10]
# lambda 매개변수목록: 식
# filter(조건함수, 컬렉션)
# list(map 또는 filter 결과)
evenNumbers = list(filter(lambda n : n%2 == 0, numbers))
print(evenNumbers)