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
print("Welcome Nmesoma Attama my tiny baby to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('you\'re on your way to the village and there are 2 two roads, choose a road.Type "left" or "right".\n '). lower()
#to ignore casing input example Right or right we can use the lower function to convert input to lowercase. to create this function put a fullstop first after the closing bracket then write the function

if choice1 == "left":
    choice2=input('you have come to a lake and there is an island in the middle of '
          'the lake. Type "wait" to wait for the oat or "swim" to swim across.\n '). lower()
    #you can divide a long sentence to shorten it for easy viewing
    if choice2 == "wait":
        choice3=input(' you arrive at the village unharmed. There is a house with 3 doors. 1 red, 1 yellow and 1 blue. Which colour do you choose?\n '). lower()
        if choice3 == "red":
            print('It is a room full of fire. Game over!')
        elif choice3 == 'yellow':
            print('You found the treasure. You Win!')
        elif choice3 == 'blue':
            print('You entered a room full of monsters. Game over!')
        else:
            print('You chose a door that does not exist. Game over!')
    else:
        print("You got attacked by a crocodile. Game over!")
else:
    print("You lose!")







