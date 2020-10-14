"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 15: Classes and Objects in Think Python 2
    
    Note: Using Python 3.9.0
"""
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


def print_point(p):
    """
        Print a point object in human readable format
    """
    print('(%g, %g)' % (p.x, p.y))


def find_center(rect):
    """
        Find the center point of a rectangle

        rect: Rectangle

        return: new Point
    """
    # Instantiate Point
    p_new = Point()
    
    # center points
    p_new.x = rect.corner.x + (rect.width / 2.0)
    p_new.y = rect.corner.y + (rect.height / 2.0)

    return p_new


def grow_rectangle(rect, d_width, d_height):
    """
        Modify a rectangles parameters

        rect: Rectangle
        d_width: float (can be negative); change in width
        d_height: float (can be negative); change in height
    """
    rect.width += d_width
    rect.height += d_height


def main():
    """
        Main function
    """
    # Instantiate Point and Rectangle
    blank = Point()
    box = Rectangle()
    box.corner = Point()

    # Initialize the Point blank
    blank.x = 3
    blank.y = 4
    print('blank', end=' ')
    print_point(blank)

    # Initialize the Rectangle box
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print("The box's width is: ", box.width)
    print("The box's height is: ",box.height)
    print("Let's grow the box.")
    grow_rectangle(box, 50, 100)
    print("The box's new width is: ", box.width)
    print("The box's new height is: ",box.height)


if __name__ == "__main__":
    main()