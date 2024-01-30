class Dog:
  def __init__(self, name, breed, age) -> None:
    self.name = name
    self.breed = breed
    self.age = age
  def sleep(self):
    print("zzzzzz.....")

class GuardDog(Dog):
  def __init__(self, name, breed) -> None:
    super().__init__(name, breed, 5)
    self.aggresive = True  
    
  def rrrrr(self):
    print("stay away!")    

# class 클래스(부모클래스):
class Puppy(Dog): 
  def __init__(self, name, breed) -> None:
    # 부모의 초기화 함수를 호출
    super().__init__(name, breed, 0.1)
    self.spoiled = True

  def woof_woof(self):
    print("Woof Woof")

ruffus = Puppy(name="Ruffus", breed="Beagle")
bibi = GuardDog(name="Bibi", breed="Dalmatian")

ruffus.woof_woof()
ruffus.sleep()

bibi.rrrrr()
bibi.sleep()