import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []

def text_state(name, xcor, ycor):
    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.speed("fastest")
    text.goto(xcor, ycor)
    text.write(name, font=("Arial", 7, "bold"))

with open("50_states.csv") as data:
    data = pandas.read_csv(data)
    states = data["state"]
    x = data["x"]
    y = data["y"]

number_states = len(states)
correct_answers = 0

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{correct_answers}/{number_states}", prompt="Digite o nome de um estado dos EUA").title()

    for state in range(0, number_states):
        if answer_state == states[state] and answer_state not in guessed_states:
            guessed_states.append(answer_state)
            correct_answers += 1
            x_cor = x[state]
            y_cor = y[state]
            text_state(answer_state, x_cor, y_cor)

        if answer_state == "Exit":
            game_is_on = False


    if correct_answers == number_states:
        game_is_on = False

if correct_answers != number_states:
    states_missing = []
    for n in range(len(states)):
        if states[n] not in guessed_states:
            states_missing.append(states[n])
    data = pandas.DataFrame({"Missing States": states_missing})
    data.to_csv("missing_states.csv", index=False)




