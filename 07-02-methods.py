class Puppy:
  # 메서드는 객체 자신을 첫번째 메서드로 받는다
  # __init__ 객체 생성시 호출
  def __init__(self, name, breed) -> None:
    self.name = name
    self.age = 0.1
    self.breed = breed
  # __str__ 문자열로 변환할 때 호출(예, 프린트)
  def __str__(self) -> str:
    return f"{self.breed} puppy named {self.name}"
  
  def woof_woof(self):
    print("Woof Woof")
  
  def introduce(self):
    self.woof_woof()
    print(f"My name is {self.name} and I am a baby {self.breed}")

ruffus = Puppy(name="Ruffus", breed="Beagle")
bibi = Puppy(name="Bibi", breed="Dalmatian")

print(ruffus, bibi)
ruffus.introduce()
bibi.introduce()

print(ruffus.name, ruffus.age, ruffus.breed)
print(bibi.name, bibi.age, bibi.breed)