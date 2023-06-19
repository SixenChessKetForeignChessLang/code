#Hello! this is my first ever program that I have written as a complete novice
#the following code may be rough around the edges but this python program bookmarks my first steps
#into the field of programming

import random

color_1 = "yellow"
color_2 = "white"
color_3 = "pink"
color_4 = "blue"
color_5 = "red"
color_6 = "green"

#random color outputs (allows replacement)
def randomized_output():
 global output
 variables = [color_1, color_2, color_3, color_4, color_5, color_6]
 selected_outputs = random.choices(variables, k=3)
 print("Winning Colors")
 for output in selected_outputs:
        print(output)
print()

#this function handles bet amount (unneeded function, keeps lang kasi for reference)
def bet_amount():
    valid_inputs = [5, 10, 20, 50, 100, 200, 500, 1000]
    
    while True:
        bet_input = input("Type in the amount you want to bet(5,10, 20, 50, 100, 200, 500, 1000): ")
        
        try:
            amount = int(bet_input)
            if amount in valid_inputs:
                print("You have bet", amount)
                break
            else:
                print("Invalid bet amount. Please choose from the following: 5, 10, 20, 50, 100, 200, 500, 1000")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    pick_color()

#this function is about the user picking what color to bet on    
def pick_color():
    colors = [color_1, color_2, color_3, color_4, color_5, color_6]
    color_bets = {}
    total_bet_amount = 0
    

    bet_input = input("Enter the color(s) and bet amount(s) separated by commas (e.g., yellow:(amount),white:(amount)): ")
    bet_inputs = bet_input.split(",")
    bet_inputs = [input.lower() for input in bet_inputs]
    for bet_input in bet_inputs:
        try:
            color, amount = bet_input.split(":")
            color = color.strip()
            amount = int(amount.strip())
            
            if color in colors and amount in [5, 10, 20, 50, 100, 200, 500, 1000]:
                if color in color_bets:
                    color_bets[color] += amount
                else:
                    color_bets[color] = amount
                total_bet_amount += amount
            else:
                print(f"Invalid input: {bet_input}. Please enter a valid color and one of the allowed bet amounts: 5, 10, 20, 50, 100, 200, 500, 1000.")
        except ValueError:
            print(f"Invalid input: {bet_input}. Please enter a valid color and a non-negative number.")

    if len(color_bets) > 1:
        evenly_distributed_amount = total_bet_amount // len(color_bets)
        remaining_amount = total_bet_amount % len(color_bets)
        print("Evenly distributed bet amounts:")
        for color, bet_amount in color_bets.items():
            distributed_amount = evenly_distributed_amount
            if remaining_amount > 0:
                distributed_amount += 1
                remaining_amount -= 1
            print(f"{color}: {distributed_amount}")
            #do other stuff with the distributed_amount
    else:
        print("Bet amounts for chosen color(s):")
        for color, bet_amount in color_bets.items():
            # Perform further operations with the 'amount' variableint(f"{color}: {bet_amount}")
            #bet_amount here and then randommized output function will be enabled
            randomized_output()

#REWARD SYSTEM 
     

#fancy looking ascii art stuff something
print ("╭╮╭━╮╱╱╭╮╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╱╱╭━━━╮")
print ("┃┃┃╭╯╱╭╯╰┳╮╱╱╱┃╭━╮┃╱╱┃┃╱╱╱╱╱╱┃╭━╮┃")
print ("┃╰╯╯╭━┻╮╭┫┣━━╮┃┃╱╰╋━━┫┃╭━━┳━╮┃┃╱╰╋━━┳╮╭┳━━╮")
print ("┃╭╮┃┃┃━┫┃╰┫━━┫┃┃╱╭┫╭╮┃┃┃╭╮┃╭╯┃┃╭━┫╭╮┃╰╯┃┃━┫")
print ("┃┃┃╰┫┃━┫╰┳╋━━┃┃╰━╯┃╰╯┃╰┫╰╯┃┃╱┃╰┻━┃╭╮┃┃┃┃┃━┫")
print ("╰╯╰━┻━━┻━┻┻━━╯╰━━━┻━━┻━┻━━┻╯╱╰━━━┻╯╰┻┻┻┻━━╯")

#user input to run the program
while True:
    user_input = input("Enter 'quit' to exit or any other input to play: ")

    if user_input.lower() == "quit":
        print("Exiting the program...")
        break

    pick_color()
