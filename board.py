from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.number = 1
        self.create()
        #self.create_numbers()

    def create(self):
        self.color("white")
        self.penup()
        self.goto(-250, -250)
        self.pendown()
        self.steps = self.ycor()
        self.goto(250, self.ycor())
        self.goto(self.xcor(), 250)
        self.goto(-250, self.ycor())
        self.goto(self.xcor(), -250)
        for i in range(-200, 250, 50):
            self.goto(-250, self.ycor())
            self.goto(self.xcor(), i)
            self.goto(250, self.ycor())

        for i in range(-200, 250, 50):
            self.goto(self.xcor(), -250)
            self.goto(i, self.ycor())
            self.goto(self.xcor(), 250)

        self.penup()
        self.goto(-250, -250)
# THIS function is optional
    def create_numbers(self):

        for _ in range(0, 10):
            if self.xcor() >= 225:
                for d in range(-225, 250, 25):
                    next = d
                    next *= -1
                    if d % 10 != 0:
                        self.goto(next, self.steps)
                        self.write(arg=self.number, align="center", font=("Arial", 15, "normal"))
                        self.number += 1
            elif self.xcor() == -225 or self.xcor() == -250:
                for d in range(-225, 250, 25):
                    if d % 10 != 0:
                        self.goto(d, self.steps)
                        self.write(arg=self.number, align="center", font=("Arial", 15, "normal"))
                        self.number += 1

            self.steps += 50
            self.hideturtle()

