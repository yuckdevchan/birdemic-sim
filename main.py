import random

Trees = 100
TreeEnergy = 10
TreeHardness = 1
TreeSpeed = TreeEnergy / TreeHardness
Seeds = 0
Seeds = Trees * TreeSpeed



while Trees < 1000:
  Trees = Seeds
  Seeds = 0
  print(Seeds)
  print(Trees)
  
