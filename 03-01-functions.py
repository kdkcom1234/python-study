# 함수 정의
def say_hello(user_name, user_age):
  print("hello", user_name, user_age)
  print("you are", user_age, "years old")

def say_bye():
  print("bye bye")

def tax_calculator(money):
  print(money * 0.35)

say_hello("nico", 30)
say_hello("ralph", 20)
say_bye()

tax_calculator(100000)