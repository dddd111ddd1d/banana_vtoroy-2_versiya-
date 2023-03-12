import requests
from colorama import Fore

class Person:
  def __init__ (self, nat, gen):
    r = requests.get("https://randomuser.me/api/?nat=" + nat + '&gender=' + gen)
    res = r.json()
    self.name = res["results"][0]["name"]["first"]
    self.surename = res["results"][0]["name"]["last"]
    self.age = res["results"][0]["dob"]["age"]
    self.phone = res["results"][0]["phone"]
    self.email = res["results"][0]["email"]
    self.isMale = res["results"][0]["gender"] == "male"
    
  def print_person(self):
    if self.isMale:
      print(Fore.CYAN)
    else:
      print(Fore.MAGENTA)
    print(self.name)
    print(self.surename)
    print(self.age)
    print(self.phone)
    print(self.email)
    print(self.isMale)

try:
  a = input("ckilku treba pratcuvnukiv?")
  a = int(a)
except:
  print("ne choje na chufru")
  a = input("ckilku treba pratcuvnukiv?")
  a = int(a)

# якої статі колектив буде
m = input("Tilku choloviku?")
gen = "male"

if m == "-":
  gen = "female"


rabotnici = []

# генеруємо колектив
while a != 0:
  n = input("vvedit nasionalnict" + a + )
  p = Person('fi', gen)
  rabotnici.append(p)
  a -= 1

# виписуємо дані про працівників
for p in rabotnici:
  p.print_person()




     