from turtle import Turtle
from dies import Dies
import time
dies = Dies()
go_left = [-225, -125, -25, 75, 175]
go_right = [-175, -75, 25, 125, 225]
class Timmy(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.game_on = True
        self.x_axis = x
        self.y_axis = y
        self.colors = color
        self.create_player()


    def create_player(self):
        self.shape("circle")
        self.color(self.colors)
        self.penup()
        self.goto(self.x_axis, self.y_axis)



    def start_position(self):

        self.goto(-225,-225)

    def player_time(self):
        dies.ram()

        with open("players.txt", "r") as computer:
            c = computer.read()
        if "pass" in c:
            print(f"player: {dies.no_dies}")
            for i in range(1, dies.no_dies + 1):

                if self.xcor() == 225 and self.ycor() in go_left:
                    y_steps1 = self.ycor() + 50
                    self.goto(self.xcor(), y_steps1)

                elif self.xcor() == -225 and self.ycor() in go_right:
                    y_steps2 = self.ycor() + 50
                    self.goto(self.xcor(), y_steps2)

                elif self.ycor() in go_right:
                    x = self.xcor() - 50
                    self.goto(x, self.ycor())

                else:
                    x = self.xcor() + 50
                    self.goto(x, self.ycor())


        else:
            if dies.no_dies == 1:
                self.start_position()
                time.sleep(1)
                print("player 1")
                with open("players.txt", "w") as computer:
                    computer.write("pass")
            else:
                print(f"player: {dies.no_dies}")
                time.sleep(1)

    def machine_time(self):
        dies.ram()

        with open("machine.txt", "r") as computer:
            c = computer.read()
        if "pass" in c:
            print(f"machine: {dies.no_dies}")
            for i in range(1, dies.no_dies + 1):

                if self.xcor() == 225 and self.ycor() in go_left:
                    y_steps1 = self.ycor() + 50
                    self.goto(self.xcor(), y_steps1)

                elif self.xcor() == -225 and self.ycor() in go_right:
                    y_steps2 = self.ycor() + 50
                    self.goto(self.xcor(), y_steps2)

                elif self.ycor() in go_right:
                    x = self.xcor() - 50
                    self.goto(x, self.ycor())

                else:
                    x = self.xcor() + 50
                    self.goto(x, self.ycor())


        else:
            if dies.no_dies == 1:
                self.start_position()
                time.sleep(1)
                print("machine 1")
                with open("machine.txt", "w") as computer:
                    computer.write("pass")
            else:
                print(f"machine: {dies.no_dies}")
                time.sleep(1)

    def check(self):
        if self.xcor() == -75 and self.ycor() == -225:
            self.goto(-25, -125)
        elif self.xcor() == 125 and self.ycor() == -175:
            self.goto(25, -25)
        elif self.xcor() == 125 and self.ycor() == -75:
            self.goto(175, -25)
        elif self.xcor() == -175 and self.ycor() == -25:
            self.goto(-125, 75)
        elif self.xcor() == 225 and self.ycor() == -25:
            self.goto(175, 75)
        elif self.xcor() == -175 and self.ycor() == 75:
            self.goto(-225, 175)
        elif self.xcor() == 75 and self.ycor() == 125:
            self.goto(175, 225)
        # snake

        if self.xcor() == 75 and self.ycor() == -125:
            self.goto(-25, -225)
        elif self.xcor() == -225 and self.ycor() == -75:
            self.goto(-125, -225)
        elif self.xcor() == -125 and self.ycor() == -25:
            self.goto(-125, -175)
        elif self.xcor() == 75 and self.ycor() == 25:
            self.goto(225, -75)
        elif self.xcor() == 25 and self.ycor() == 75:
            self.goto(-25, -25)
        elif self.xcor() == -25 and self.ycor() == 125:
            self.goto(-125, 25)
        elif self.xcor() == 175 and self.ycor() == 175:
            self.goto(125, 25)
        elif self.xcor() == -175 and self.ycor() == 225:
            self.goto(-225, -25)





