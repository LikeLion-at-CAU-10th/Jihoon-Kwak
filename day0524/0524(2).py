#function that the player changes the door

def change_door(goat, player_choice) :
  i = 1
  while (i == goat or i == player_choice) :
    i = (i+1) % 3
  
  return i


print (change_door(0, 1))