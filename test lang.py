import random

color_1 = "yellow"
color_2 = "white"
color_3 = "pink"
color_4 = "blue"
color_5 = "red"
color_6 = "green"

def randomized_output():
 variables = [color_1, color_2, color_3, color_4, color_5, color_6]
 selected_outputs = random.choices(variables, k=3)
 print("Randomized output:")
 for output in selected_outputs:
        print(output)
print()

print ("place your bets on " + color_1 + ", " + color_2 + ", " + color_3 + ", " + color_4 + ", " + color_5 + ", " + color_6)
while True:
    user_input = input("Enter 'quit' to exit or any other input to continue: ")

    if user_input.lower() == "quit":
        print("Exiting the program...")
        break

    randomized_output()
