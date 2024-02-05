from turtle import Turtle, Screen
import pandas

yvan = Screen()
yvan.screensize(False, False)

yvan.addshape("blank_states_img.gif")
ks = Turtle()
ks.shape("blank_states_img.gif")
data = pandas.read_csv("50_states.csv")
state_data = data.state
state_list = state_data.to_list()
print(state_list)

state_record = []
while len(state_record) < 50:
    user_input = yvan.textinput(title="Guess a State", prompt="Which USA do you know ?").title()
    if user_input in state_list:
        rik = Turtle()
        coordinates = data[data.state == user_input]
        rik.hideturtle()
        rik.penup()
        rik.goto(int(coordinates.x), int(coordinates.y))
        rik.write(user_input)
        state_record.append(user_input)

    if user_input == "Exit":
        states_to_learn = [state for state in state_list if state not in state_record]
        save = pandas.DataFrame(states_to_learn)
        save_file = save.to_csv(index=False)
        with open("\Desktop\My Daily Projects\states_to_learn.csv", "w") as data_file:
            data_file.write(save_file)
        break

yvan.exitonclick()
