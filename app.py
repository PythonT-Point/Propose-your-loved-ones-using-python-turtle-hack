from turtle import *
# Import turtle package
import turtle as tur
  
# Creating a turtle object(turt)
turt = tur.Turtle()
tur.title("Pythontpoint")

  
# Defining a method to draw curve
def curve():
    for i in range(200):
  
        # Defining step by step curve motion
        turt.right(1)
        turt.forward(1)
  
# Defining method to draw a full heart
def heart():
  
    # Set the fill color to red
    turt.fillcolor('red')
  
    # Start filling the color
    turt.begin_fill()
  
    # Draw the left line
    turt.left(140)
    turt.forward(113)
  
    # Draw the left curve
    curve()
    turt.left(120)
  
    # Draw the right curve
    curve()
  
    # Draw the right line
    turt.forward(112)
  
    # Ending the filling of the color
    turt.end_fill()
  
# Defining method to write text
def txt():
  
    # Move turtle to air
    turt.up()
  
    # Move turtle to a given position
    turt.setpos(-68, 95)
  
    # Move the turtle to the ground
    turt.down()
  
    # Set the text color to lightgreen
    turt.color('cyan')
  
    # Write the specified text in 
    # specified font style and size
    turt.write("I Love You", font=(
      "Times New Roman", 12, "bold"))
  
  
# Draw a heart
heart()
  
# Write text
txt()
  
# To hide turtle
tur.ht()
tur.done()