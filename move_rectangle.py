"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 15: Classes and Objects in Think Python 2
    
    Note: Using Python 3.9.0
"""
import copy
import math


class Point:
    """
        Represent a point in 2d space with x-y coordinates

        attributes: x, y
    """


class Rectangle:
    """
        Represents a rectangle in 2d space with x-y coordinates

        attributes: width, height, corner [Point]
    """


def distance_between_points(p1, p2):
    """
        Find the distance between two points

        p1: Point
        p2: Point

        return: float; distance between p1 and p2
    """
    dx = p1.x - p2.x
    dy = p1.y - p2.y

    return math.sqrt(dx**2 + dy**2)


def move_rectangle1(rect, dx, dy):
    """
        Move a Rectangle by modifying its corner attribute

        rect: Rectangle
        dx: float; change in x-coordinate (can be negative)
        dy: float; change in y-coordinate (can be negative)
    """
    rect.corner.x += dx
    rect.corner.y += dy


def move_rectangle2(rect, dx, dy):
    """
        Return a new Rectangle at the new coordinates

        rect: Rectangle
        dx: float; change in x-coordinate (can be negative)
        dy: float; change in y-coordinate (can be negative)

        return: new Rectangle
    """
    # Instantiate Rectangle by copying the existing rectangle
    new_rectangle = copy.deepcopy(rect)
    move_rectangle1(new_rectangle, dx, dy)
    
    return new_rectangle


def main():
    """
        main function
    """
    # Instantiate objects
    blank = Point()
    grosse = Point()
    box = Rectangle()

    # Initialize the Point blank
    blank.x = 0
    blank.y = 0

    # Initialize the Point grosse
    grosse.x = 3
    grosse.y = 4

    print('The distance between two points is:', end=' ')
    print(distance_between_points(blank, grosse))

    # Initialize the Rectangle box
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print("The box's x-coordinate is: %g" % (box.corner.x))
    print("The box's y-coordinate is: %g" % (box.corner.y))
    print("Now let's move the box using the first method.")
    move_rectangle1(box, 50, 100)
    print("The box's new x-coordinate is: %g" % box.corner.x)
    print("The box's new y-coordinate is: %g" % box.corner.y)

    # Instantiate a new box
    print("Now let's try the second method by creating a new rectangle.")
    new_box = move_rectangle2(box, 50, 100)
    print("The new box's x-coordinate is: %g" % new_box.corner.x)
    print("The new box's y-coordinate is: %g" % new_box.corner.y)


if __name__ == "__main__":
    main()