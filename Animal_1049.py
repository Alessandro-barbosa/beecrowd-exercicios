primeiro = input()
segundo = input()
terceiro = input()
nVertebrado = "vertebrado"
nInvertebrado = "invertebrado"

vertebrado = {
  
  "ave":{
    "carnivoro": "aguia",
    "onivoro": "pomba"
  },
  "mamifero":{
    "onivoro": "homem",
    "herbivoro": "vaca"
  },
}

invertebrado = {
  "inseto": {
    "hematofago": "pulga",
    "herbivoro": "lagarta"
  },
  "anelideo":{
    "hematofago": "sanguessuga",
    "onivoro": "minhoca"
  }
}

if(primeiro == nVertebrado):
  for x in vertebrado:
    if(segundo == x):
      for y in vertebrado[x]:
        if(terceiro == y):
          print(vertebrado[x][y])

if(primeiro == nInvertebrado):
  for x in invertebrado:
    if(segundo == x):
      for y in invertebrado[x]:
        if(terceiro == y):
          print(invertebrado[x][y])