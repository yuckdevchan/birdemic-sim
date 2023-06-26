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


while Trees < 1000:
  Check1 = random.randint(0, 3)
  if Check1 == 2:
  TreeMutation1 = random.randint(0, 5)
  TreeMutation1 = TreeMutation1 / 100
  TreeHardness -= TreeMutation1
  Trees = Seeds
  Seeds = 0
  print(Seeds)
  print(Trees)

sys.exit
