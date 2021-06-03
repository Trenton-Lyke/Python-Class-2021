# This is a comment.
# By putting a hashtag (#) at the beginning of a line,
# I tell the computer that this line does not contain
# any code that should be run. 
""" 
    I can also use 3 quotation marks to write multi-line
    comments. This allows me to tell the computer to 
    ignore all that I type up until the next 3 quotation 
    marks as seen below.
"""
# You will see a lot of comments in this course to help
# you with different coding activities

""" 
    Activity 1: Hello World
    In most programming languages, like Python,
    you will be able to print out text in a window called
    the terminal (also called console or shell sometimes).

    To print text in python we use the print() function.
    Python will display the argument given to the function
    or in other words whatever we put between the parantheses
    of the function.
"""

# 1. Run the code below to see what is printed out in the terminal.
#    You can do this by saving the file, clicking the "Run" tab at 
#    the top, and then click the "Run Module" option in the drop down menu.
print("I want to let the world know I'm here")



"""
    Wait why weren't the quotations displayed? That's
    because Python only cares about the text enclosed
    by the quotation marks ("). The quotation marks are 
    only there to help Python distinguish between text-based 
    code and text-based data. You can also replace the 
    quotation marks (") with apostrophes (') if you like.
"""

# 2. Uncomment the line of code with the print() function 
#    below by removing the hashtag (#) at the beginning of the 
#    line so that your computer will know to run the code.
#    Then run the code.

#print('I still want to let the world know I am here!')




"""
    Did you notice that I replaced "I'm" with "I am" in the
    second output. That's becauese the second time the 
    apostrophe (') was being used to indicate that the
    statement was data rather than code. The currently
    commented out code:
    print('I still want to let the world know I'm here!')
    would cause an error because Python would mistake everything
    after the second apostrophe (i.e. "m here!") as code.

    There is a way around this with the escape character
    also known as the backslash (\). By placing a backslash in
    front of an apostrophe or a quotation mark we tell Python
    to treat the apostrophe as part of the text rather than the 
    indicator of the end of the text.
"""
#3. Uncomment the line of code with the print() function 
#   below. Try running the code now.
#   *hint: you might not be able to
#   Then escape the second apostrophe (') in I'm by
#   adding a backslash (\) in front of the apostrophe
#   like so I\'m. Finally run the code. 
#print('I still want to let the world know I'm here!')



#4. Final Challenge: Write a line of code below to print 
#   out the phrase "Hello World" in the terminal.
#   Note: You don't have to display the quotation marks (")
#   in the terminal if you don't want to.




#5. Optional Activity (Ignore this unless you're bored):
#   Try out "Python Shell" by clicking the "Run" tab at 
#   the top and then clicking the "Python Shell" option.
#   If you type a line of python code after the triple 
#   greater than signs (>>>) and hit enter, then your
#   code will run. Try running the line of code:
#   print("Hi I'm a computer")
