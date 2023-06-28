import random
import sys

Trees = 100
TreeEnergy = 10
TreeHardness = 1
TreeSpeed = TreeEnergy / TreeHardness
Seeds = 0
Seeds = Trees * TreeSpeed
Check1 = 0
TreeMutation1 = 0
limit = 1000000
Birds = 10
BirdSpeed = 3
BirdEat = Birds * BirdSpeed
BirdAllEat = 10

while Trees < limit:
  Seeds = Trees * TreeSpeed
  BirdEat = Birds * BirdSpeed
  Seeds -= BirdEat
  print(f"trees: {Trees}")
  print(f"seeds: {Seeds}")
  Check1 = random.randint(0, 3)
  if Check1 == 2:
    TreeMutation1 = random.randint(0, 2) / 100
    TreeHardness -= TreeMutation1
  Trees = Seeds
  Seeds = 0
  

print(f"Reached limit: {limit}")
sys.exit
