from math import sqrt, sin, cos, asin, acos, pi

__all__ = ["legit_angle", "get_side_from_sin_theorem", "get_side_from_2_sides", "get_third_angle", "sqrt", "sin",
           "get_angle_from_3_sides", "get_angle_from_3_sides", "get_angle_from_height_and_side", "get_height",
           "get_surface", "get_median", "get_bisector", "get_outer_radius", "get_inner_radius", "pi", "cos"]

def legit_angle(angle, given=0):
    return 0 < angle < pi - given


def get_side_from_sin_theorem(side, angle, opposite_angle):
    return side * sin(opposite_angle) / sin(angle)


def get_side_from_2_sides(side_1, side_2, angle):
    return sqrt(side_1 ** 2 + side_2 ** 2 - 2 * side_1 * side_2 * cos(angle))


def get_third_angle(angle_1, angle_2):
    return pi - angle_1 - angle_2


def get_angle_from_3_sides(opposite, side_1, side_2):
    return acos((side_1 ** 2 + side_2 ** 2 - opposite ** 2) / (2 * side_1 * side_2))


def get_angle_from_height_and_side(height1, side2):
    return asin(height1 / side2)


def get_height(surface, side):
    return 2 * surface / side


def get_surface(side_1, side_2, side_3):
    return sqrt((side_1 + side_2 + side_3) * (side_2 + side_3 - side_1) * (side_1 - side_2 + side_3) * (
            side_1 + side_2 - side_3)) / 4


def get_median(opposite, side_1, side_2):
    return sqrt((2 * (side_1 ** 2 + side_2 ** 2) - opposite ** 2)) / 2


def get_bisector(angle, side_1, side_2):
    return 2 * side_1 * side_2 * cos(angle / 2) / (side_1 + side_2)


def get_outer_radius(side, angle):
    return side / (2 * sin(angle))


def get_inner_radius(surface, perimeter):
    return 2 * surface / perimeter
