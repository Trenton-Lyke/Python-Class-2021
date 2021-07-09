from turtle import *

triangle_turtle = Turtle()
triangle_turtle.shape('turtle')


# First Way of drawing a triange (a lot of code)

# triangle_turtle.right(120) is a new method call that we haven't seen before.
# The method call causes the turtle icon to turn to the right 120 degrees the 
# 120 coming from argument between the method calls parentheses
triangle_turtle.right(120)
triangle_turtle.forward(300)
triangle_turtle.right(120)
triangle_turtle.forward(300)
triangle_turtle.right(120)
triangle_turtle.forward(300)


# Second Way of drawing a triange (For loop what makes computers awesome)

# The code below is what we call a for loop. It repeats a "block" of code a 
# certain number of times. In this case the "block of code" is repeated 3 times.
# The 3 coming from the argument between the parentheses of the range() function call.

# The "block" of code that it repeats are the consequtive 
# lines of code that are all indented. In this example, the "block" of code includes
# the lines:
#    triangle_turtle.right(120)
#    triangle_turtle.forward(300)
# so that code is repeated, but the line of code:
# print("done with triangle")
# is outside of that block because it is not indented so that code is not repeated
for i in range(3):
    triangle_turtle.right(120)
    triangle_turtle.forward(300)
print("done with triangle")


# Third Way of drawing a triangle (While loop more awesome in other situations)

# The code below is what we call a while loop. It repeats also a "block" of code a, 
# but unlike a for loop it repeats the code while a certain condition is True. 
# In this case, the condition for the "block of code" to repeat is that the variable 
# increasing_number has a value that is less than (<) 3 which comes from the statement
# while increasing_number < 3. Since the increasing_number variables value starts at 0 
# and is increased by 1 at the end of the block of code that gets repeated due to the 
# line of code:
#    increasing_number = increasing_number + 1
# after code block is executed 3 time the increasing_number variables value will be 3
# and since 3 < 3 is False the code block will not repeat again in the while loop after
# that.
# The condition of the while look causes the code block to be repeated 3
increasing_number = 0
while increasing_number < 3:
    triangle_turtle.right(120)
    triangle_turtle.forward(300)
    increasing_number = increasing_number + 1