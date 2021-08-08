import time
from turtle import Screen
from board import Board
from player import Timmy

player = Timmy(-50, -290, "blue")
machine = Timmy(50, -290, "red")
screen = Screen()
screen.tracer(0)
snake_board = Board()
screen.setup(800, 800)
screen.bgpic("snake1.gif")

with open("machine.txt","w") as file:
    file.write("")
with open("players.txt","w") as file:
    file.write("")


while True:
    PLAYER_VALUE = player.xcor()
    MACHINE_VALUE = machine.xcor()

    time.sleep(0.1)
    screen.update()
    screen.textinput("Snake Hai", "Name of first player:")
    # time.sleep(1)
    player.player_time()
    if player.ycor() > 225:
        player.goto(PLAYER_VALUE, 225)

    machine.machine_time()
    if machine.ycor() > 225:
        machine.goto(MACHINE_VALUE, 225)

    player.check()
    machine.check()




