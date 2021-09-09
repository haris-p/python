class Hero:

  angka = 0
  def __init__(self,namahero,powerhero,powerhealt,armornumber):
    self.nama = namahero
    self.power = powerhero
    self.healt = powerhealt
    self.armor = armornumber
    Hero.angka += 1 
    print(Hero.angka)

  def siapa(self):
    print("ini adalah: " + self.nama)

  def healtup(self,up):
    self.healt += up 

hero1 = Hero("ucup",100,20,30)
hero2 = Hero("dejong",90,30,20)

print(hero1.__dict__)
hero1.siapa()

print(hero2.__dict__)
hero1.healtup(20)
print(hero1.healt)