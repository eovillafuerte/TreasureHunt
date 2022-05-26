print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


cross_roads = input('Where do you want to go? left or right\n')

if cross_roads == "left":
  print('Sliced by General Grievous.You lose Kenobi!')
elif cross_roads == "right":
  print('made it to lake')
  
  lake_decision = input ('so do you want to wait or swim?\n')
  if lake_decision == "swim":
    print ('made it to the final level')
    final_decision = input('Choose the stairs, hole, speeder, or walkaway.\n')
    if final_decision == "stairs":
      print('Lord sideous appears and you lose')
    elif final_decision == 'hole':
          print('Congratulations, you found the dark saber and you saved the galaxy!')
    elif final_decision == 'speeder':
            print('order 66 is executed')
    else: 
      print('army or not, you must realise you are doomed!')
     
  elif lake_decision == "wait":
      print('blasted by clonetroopers')