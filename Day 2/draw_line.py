# Grabs a buch of previous programmers code so we can use the Turtle Module
# Read as: from turtle import all
from turtle import *


# In the line of code below our_first_turtle is what we call a variable.
# A variable is a place for a value. The variable our_first_turtle uses 
# underscores (_) instead of spaces in its name because Python doesn not 
# allow spaces in a Python variable. In this case the variable 
# our_first_turtle is holding a Turtle object as its value. Think of an 
# object as something you can observe and do things with in coding. Turtle() 
# is a constructor. Turtle() constructs/makes a Turtle object. The equal sign 
# tells the computer to save the Turtle object in the our_first_turtle 
# variable for later use.
our_first_turtle = Turtle()


# The line of code below is what is known as a calling a method on an object
# also referred to as a method call. Consider a method call as something we 
# can do with an object in coding. The method call below makes the drawing 
# icon a turtle as you will see later.

# To call a method on an object. You need to
# first type the name of the variable holding the object (our_first_turtle in 
# our case) then put a period (.) the name of the method you want to call 
# (shape in our case) and the finally the parentheses containing any arguments
# ('turtle') in our case.
our_first_turtle.shape('turtle')


# The line of code below is another method call, but this one move the turtle
# icon forward 300 pixels the 300 coming from the argument between the method
# calls parentheses
our_first_turtle.forward(300)