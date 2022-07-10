import random
from turtle import Turtle


def recursive_conch( turtle, angle, quantity, delta, radius ):
    turtle.color("Navy")
    turtle.right(angle)
    turtle.forward(delta)
    unit = 360.0/quantity
    for x in range(quantity):
        turtle.circle(radius)
        turtle.left(unit)
        turtle.right(unit - 5)
    radius = radius - delta
    if( radius > 5 ):
        recursive_conch(turtle, angle, quantity, delta, radius)
        
def main():
    ANIMATION_SPEED = 0
    leonardo = Turtle()
    leonardo.speed(ANIMATION_SPEED)
    recursive_conch(leonardo, 45, 7, 6, 200)

main()
    
