import turtle
import pandas
import string

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
cursor = turtle.Turtle()
cursor.penup()
cursor.hideturtle()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()


def turtle_write(a, b, state_name):
    cursor.goto(a, b)
    cursor.write(f"{state_name}", align="center", font=("Calibri", 13, "normal"))


correct_guesses = 0
while correct_guesses < 50:
    answer_state = screen.textinput(title=f"{correct_guesses}/50 correct", prompt="What's another state name?")
    answer_state = string.capwords(answer_state)
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        correct_guesses += 1
        coordinates = data[data["state"] == answer_state].to_dict()
        state_num = list(coordinates["state"].keys())[0]
        x = coordinates["x"][state_num]
        y = coordinates["y"][state_num]
        turtle_write(x, y, answer_state)


