# from 패키지 import 함수
from random import randint

user_choice = int(input("Choose number."))
pc_choice = randint(1, 50) # 1 ~ 50사이 랜덤 정수

if user_choice == pc_choice:
  print("You won!")
elif user_choice > pc_choice:
  print("Lower! Computer chose", pc_choice)
elif user_choice < pc_choice:
  print("Higher! Computer chose", pc_choice)
