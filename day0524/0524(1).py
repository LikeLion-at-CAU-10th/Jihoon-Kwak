# THe goat door that Monty shows


def goat_door (car_door, player_choice) :
  i = 1
  while (i == car_door or i == player_choice) :
    i = (i+1) % 3
    print("I inside while loop = ", i)
  return i


print ( goat_door (0, 1))