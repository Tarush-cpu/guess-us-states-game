import csv
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"C:\Users\CJCte\Downloads\day-25-us-states-game-start\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


writer = turtle.Turtle()
writer.hideturtle()
writer.penup()


state_data = {}
with open(r"C:\Users\CJCte\Downloads\day-25-us-states-game-start\50_states.csv") as data_file:
    data = csv.reader(data_file)
    next(data) 
    for row in data:

        state_data[row[0]] = (int(row[1]), int(row[2]))

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break

    if answer_state in state_data:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            coords = state_data[answer_state]
            writer.goto(coords)
            writer.write(answer_state, align="center", font=("Arial", 8, "normal"))

screen.exitonclick()

