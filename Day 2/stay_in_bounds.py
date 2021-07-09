from turtle import *
# just imports previous programmers code so I can randomize some stuff for you
from random import *

square_turtle = Turtle()
square_turtle.shape('turtle')

# randomizes your turtles starting position
square_turtle.goto(randint(-screensize()[0],screensize()[0]),0)

# for loop repeats 100 time
for i in range(1000):

    # what you see below is an if-elif-else chain (also referred to as if-elif-else 
    # statements). The if-elif-else chain allows you to tell the computer to run 
    # code blocks if a certain condition is met. It is similar to a while loop, but the
    # code block is only executed once. 

    # The first part of the chain, the if statement, checks if a condition is True. If it
    # is True then its corresponding code block is executed and the computer moves past the 
    # rest of the if-elif-else chain, but if it is False then the 
    # computer moves down the chain to the elif statement. The condition that is being 
    # checked in the first if statement: 
    #   square_turtle.position()[0] > screensize()[0]
    # basically just checks if the turtle has hit the right side of the screen.
    # elif is short for else if, which you may see in other programming languages.

    # Just like the if statement, the elif statement checks if a condition is True. If it
    # is True then its corresponding code block is executed and the computer moves past the 
    # rest of the if-elif-else chain, but if it is False then the 
    # computer moves down the chain to another elif statement or in this case the else 
    # statement. The condition that is being checked in the first if statement: 
    #   square_turtle.position()[0] > screensize()[0]
    # basically just checks if the turtle has hit the left side of the screen.

    # Lastly if the computer reaches the else statement then the corresponding code block
    # is executed without checking a condition
    if square_turtle.position()[0] > screensize()[0]:
        #turns the turtle around
        square_turtle.right(180)
        #moves the turtle forward 5 pixels
        square_turtle.forward(5)
    elif square_turtle.position()[0] < -screensize()[0]:
        #turns the turtle around
        square_turtle.right(180)
        #moves the turtle forward 5 pixels
        square_turtle.forward(5)
    else:
        #moves the turtle forward 5 pixels
        square_turtle.forward(5)