print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
path = input("The path you're walking diverges, go 'left' or 'right' ")
if path == 'left' or 'Left':
    river = input('The path ends at a large river, "swim" or "wait" for a boat ride ')
    if river == 'wait' or 'Wait':
        door = input("You land on the other side of the river and see a 'blue', 'red', and 'yellow' door. Choose wisely ")
        if door == "yellow" or "Yellow":
            print("You win! Congrats")
        elif door == 'red' or 'Red':
            print('The room you walk into quickly engulfs in flame. GAME OVER')
        elif door == 'blue' or 'Blue':
            print('As u walk in, a lion attacks you from behind. GAME OVER')
    else: print("As you swim, you're viciously attacked by a school of Trout. GAME OVER")
else: print("You go right and fall into a conveniently place 20ft hole. GAME OVER")