"""
    This module contains code related to
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to complete the exercises in Chapter 15: Classes and Objects in Think Python 2
    
    Note: Using Python 3.9.0
"""
import math
import copy


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


def point_in_circle(p, cir):
    """
        Determine if a given point is within the radius of a circle
        
        p: Point
        cir: Circle
        
        return: boolean; True if point is within the circle, false otherwise
    """
    distance = distance_between_points(p, cir.center)
    return distance <= cir.radius


def rectangle_in_circle(cir, rect):
    """
        Deterine if a rectangle fits entirely within the circle

        cir: Circle
        rect: Rectangle

        return: boolean; True if all points of the rectangle fit within the circle, false otherwise
    """
    p = copy.copy(rect.corner)
    if not point_in_circle(p, cir):
        return False
    
    p.x += rect.width
    if not point_in_circle(p, cir):
        return False
    
    p.y -= rect.height
    if not point_in_circle(p, cir):
        return False
    
    p.x -= rect.width
    if not point_in_circle(p, cir):
        return False
    
    return True


def rectangle_circle_overlap(cir, rect):
    """
        Determine if there is any overlap of the circle and rectangle

        cir: Circle
        rect: Rectangle

        return: boolean; True if the circle and rectangle overlap, false otherwise
    """
    # Determine if the rectangle fits entirely within the circle
    if rectangle_in_circle(cir, rect):
        return True

    # Instantiate point
    p1 = copy.copy(rect.corner)
        
    # Determine if any of the points fall within the circle
    if point_in_circle(p1, cir):
        return True
    
    # Intantiate new point
    p2 = copy.copy(rect.corner)
    p2.x += rect.width
    if point_in_circle(p2, cir):
        return True
    
    # Intantiate new point
    p3 = copy.copy(p2)
    p3.y -= rect.height
    if point_in_circle(p3, cir):
        return True
    
    # Intantiate new point
    p4 = copy.copy(p3)
    p4.x -= rect.width
    if point_in_circle(p4, cir):
        return True
    
    # Determine if any of the lines cross the circle
    if (line_circle_intersect(cir, p1, p2)) or (line_circle_intersect(cir, p2, p3)) or (line_circle_intersect(cir, p3, p4)) or (line_circle_intersect(cir, p3, p4)):
        return True

    # Determine if the rectangle encompasses the circle
    if circle_in_rectangle(cir, rect):
        return True
    
    # If none of the other conditions fit, then there is no overlap
    return False


def line_circle_intersect(cir, p1, p2):
    """
        Determine if a line intersects, crosses or touches, a circle

        cir: Circle
        p1: Point
        p2: Point

        return: boolean; True if the line between p1 and p2 intersects the circle, false otherwise

        Note: uses the distance from a point to a line equation found on wiki
            https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    """
    # Copy the circle
    cir_copy = copy.deepcopy(cir)
    distance = (abs(((p1.y - p2.y) * cir_copy.center.x) - ((p1.x - p2.x) * cir_copy.center.y) + (p2.x * p1.y) - (p2.y * p1.x))) / (math.sqrt(((p2.y - p1.y)**2) + ((p2.x - p1.x)**2)))

    if (cir_copy.radius >= distance):
        return True
    return False


def circle_in_rectangle(cir, rect):
    """
        Determine if a circle is within a rectangle

        cir: Circle
        rect: Rectangle

        return: boolean; True if circle is within a rectangle, false otherwise
    """
    # Copy the objects
    new_cir = copy.deepcopy(cir)
    p1 = copy.copy(rect.corner)

    # Instantiate and initialize new point
    p2 = Point()
    p2.x = p1.x + p1.width
    p2.y = p1.y - p1.height

    # Find the nearest point on the rectangle to the center of the circle
    xn = max(p1.x, min(new_cir.center.x, p2.x))
    yn = max(p1.y, min(new_cir.center.y, p2.y))

    """
        Find the distance between the nearest point and the center of the circle
        Distance between 2 points, (x1, y1) & (x2, y2) in 2d Euclidian space is:
        ((x1-x2)**2 + (y1-y2)**2)**0.5
    """
    dx = xn - new_cir.center.x
    dy = yn - new_cir.center.y

    return (dx**2 + dy**2) <= (new_cir.radius)**2


def main():
    """
        main function
    """
    # Instantiate and initialize a rectangle
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print("The rectangle's x-coordinate is: %g" % box.corner.x)
    print("The rectangle's y-coordinate is: %g" % box.corner.y)
    print("The rectangle's width is: %g" % box.width)
    print("The rectangle's height is: %g" % box.height)

    # Instantiate and initialize a Circle
    circle = Circle()
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print("The center x-coordinate of the circle is: %g" % circle.center.x)
    print("The center y-coordinate of the circle is: %g" % circle.center.y)
    print("The radius of the circle is: %g" % circle.radius)

    print("The initial corner of the rectangle is in the circle: ", point_in_circle(box.corner, circle))
    print("The rectangle is completely in the circle: ", rectangle_in_circle(circle, box))
    print("The rectangle and circle overlap: ", rectangle_circle_overlap(circle, box))


if __name__ == '__main__':
    main()