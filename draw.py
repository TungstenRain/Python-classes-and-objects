"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 15: Classes and Objects in Think Python 2
    
    Note: Using Python 3.9.0
"""
import turtle
import polygon


class Point:
    """
        Represent a point in 2d space with x-y coordinates

        attributes: x, y
    """


class Circle:
    """
        Represents a circle in 2d space

        Attributes: center [Point], radius
    """


class Rectangle:
    """
        Represents a rectangle in 2d space with x-y coordinates

        attributes: width, height, corner [Point]
    """

def draw_circle(t, circle):
    """
        Draw a circle

        t: Turtle
        c: Circle
    """
    t.pu()
    t.goto(circle.center.x, circle.center.y)
    t.fd(circle.radius)
    t.lt(90)
    t.pd()
    polygon.circle(t, circle.radius)


def draw_rect(t, rect):
    """
        Draw a rectangle

        t: Turtle
        rect: Rectangle
    """
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.setheading(0)
    t.pd()

    for length in rect.width, rect.height, rect.width, rect.height:
        t.fd(length)
        t.rt(90)

if __name__ == "__main__":
    # Instantiate Turtle
    bob = turtle.Turtle()

    # draw the axes
    length = 400
    bob.fd(length)
    bob.bk(length)
    bob.lt(90)
    bob.fd(length)
    bob.bk(length)

    # Instantiate and initialize Rectangle
    rect = Rectangle()
    rect.corner = Point()
    rect.corner.x = 50.0
    rect.corner.y = 50.0
    rect.width = 100
    rect.height = 200

    # Instantiate and initialize Circle
    circ = Circle()
    circ.center = Point()
    circ.center.x = 150.0
    circ.center.y = 150.0
    circ.radius = 75.0

    # Hide bob
    bob.hideturtle()

    # draw objects
    draw_rect(bob, rect)
    draw_circle(bob, circ)

    turtle.mainloop()