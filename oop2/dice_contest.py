from cheatdice import *

swapper = Cheat_Swapper()
loaded_dice = Cheat_Loaded_Dice()
mulligan = Cheat_Mulligan()
extra_die = Cheat_Extra_Die()

swapper_score = 0
loaded_dice_score = 0
mulligan_score = 0
extra_die_score = 0
number_of_games = 100000
game_number = 0
print("Simulation running")
print("==================")
while game_number < number_of_games:
  swapper.roll()
  loaded_dice.roll()
  mulligan.roll()
  extra_die.roll()

  swapper.cheat()
  loaded_dice.cheat()
  mulligan.cheat()
  extra_die.cheat()

   #Remove # before print statements to see simulation running
   #Simulation takes approximately one hour to run with print
   #statements or ten seconds with print statements
   #commented out

 #print("Cheater 1 rolled" + str(swapper.get_dice()))
 #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
  if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) == sum(mulligan.get_dice()) == sum(extra_die.get_dice()):
 #print("Draw!")
    pass
  elif sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) or sum(swapper.get_dice()) == sum(mulligan.get_dice()) or sum(swapper.get_dice()) == sum(extra_die.get_dice()):
    pass
  elif sum(loaded_dice.get_dice()) == sum(mulligan.get_dice()) or sum(loaded_dice.get_dice()) == sum(extra_die.get_dice()):
    pass
  elif sum(mulligan.get_dice()) == sum(extra_die.get_dice()):
    pass
  elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) > sum(mulligan.get_dice()) and sum(swapper.get_dice()) > sum(extra_die.get_dice()):
 #print("Dice swapper wins!")
    swapper_score+= 1
  elif sum(loaded_dice.get_dice()) > sum(swapper.get_dice()) and sum(loaded_dice.get_dice()) > sum(mulligan.get_dice()) and sum(loaded_dice.get_dice()) > sum(extra_die.get_dice()):
    loaded_dice_score += 1
  elif sum(mulligan.get_dice()) > sum(swapper.get_dice()) and sum(mulligan.get_dice()) > sum(loaded_dice.get_dice())  and sum(mulligan.get_dice()) > sum(extra_die.get_dice()):
    mulligan_score += 1
  else:
    extra_die_score += 1
 #print("Loaded dice wins!")

  game_number += 1
print("Simulation complete")
print("-------------------")
print("Final scores")
print("------------")
print("Swapper won: " + str(swapper_score))
print("Loaded dice won: " + str(loaded_dice_score))
print("Mulligan won: " + str(mulligan_score))
print("Extra die won: " + str(extra_die_score))

if swapper_score == loaded_dice_score == mulligan_score == extra_die_score:
  print("Game was drawn")
elif swapper_score > loaded_dice_score and swapper_score > mulligan_score and swapper_score > extra_die_score:
  print("Swapper won most games")
elif loaded_dice_score > swapper_score and loaded_dice_score > mulligan_score and loaded_dice_score > extra_die_score:
  print("Loaded dice won most games")
elif mulligan_score > swapper_score and mulligan_score > loaded_dice_score and mulligan_score > extra_die_score:
  print("Mulligan won most games")
else:
  print("Extra die won most games")
