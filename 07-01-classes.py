class Puppy:
  # 메서드는 객체 자신을 첫번째 메서드로 받는다
  # __init__ 객체 생성시 호출
  def __init__(self) -> None:
    self.name = "Ruffus"
    self.age = 0.1
    self.breed = "Beagle"

ruffus = Puppy()
bibi = Puppy()

print(ruffus.name, ruffus.age, ruffus.breed)