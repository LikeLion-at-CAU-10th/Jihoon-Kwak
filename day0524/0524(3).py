import random


# THe goat door that Monty shows


def goat_door (car_door, player_choice) :
  i = 1
  while (i == car_door or i == player_choice) :
    i = (i+1) % 3
    print("I inside while loop = ", i)
  return i


#function that the player changes the door


def change_door(goat, player_choice) :
  i = 1
  while (i == goat or i == player_choice) :
    i = (i+1) % 3
  
  return i


random.seed() #PureRandom

nwin = 0
ngame = 0

for j in range(0, 10000) : #10번의 게임 진행
  car_door          =  random.randint(0, 2) # random choice among 0, 1, 2
  player_choice     =  random.randint(0, 2) # random choice among 0, 1, 2
  goat              =  goat_door (car_door, player_choice) # monty shows
  # player_new_choice = change_door (goat, player_choice)
  player_new_choice = player_choice


  print("Car = ", car_door, ", Player = ", player_choice, ", Monty shows = ", goat, ", Chage = ",player_new_choice)


  if (car_door == player_new_choice) :
    nwin += 1

  ngame+=1

print("Game =", ngame, ",Win =", nwin)