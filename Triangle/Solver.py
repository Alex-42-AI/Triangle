from Triangle.Functions import *


def rotate_right(ls):
    if len(ls) == 2:
        return rotate_right(ls[0]), rotate_right(ls[1])
    return [ls[2], ls[0], ls[1], ls[5], ls[3], ls[4], ls[8], ls[6], ls[7], ls[9], ls[10], ls[13], ls[11], ls[12], ls[16], ls[14], ls[15], ls[17], ls[18]]


def switch_1_and_2(ls):
    if len(ls) == 2:
        return switch_1_and_2(ls[0]), switch_1_and_2(ls[1])
    return [ls[0], ls[2], ls[1], ls[3], ls[5], ls[4], ls[6], ls[8], ls[7], ls[9], ls[10], ls[11], ls[13], ls[12], ls[14], ls[16], ls[15], ls[17], ls[18]]


def side_angle_side1(side, side1, angle, angle1, angle2, h, h1, h2):
    R = get_outer_radius(side, angle)
    if side == h2 or side >= side1:
        side2 = sqrt(side ** 2 - h2 ** 2) + sqrt(side1 ** 2 - h2 ** 2)
        angle1 = get_angle_from_3_sides(side1, side, side2)
        angle2 = get_third_angle(angle, angle1)
        P = side + side1 + side2
        S = get_surface(side, side1, side2)
        h = get_height(S, side)
        h1 = get_height(S, side1)
        m = get_median(side, side1, side2)
        m1 = get_median(side1, side, side2)
        m2 = get_median(side2, side, side1)
        b = get_bisector(angle, side1, side2)
        b1 = get_bisector(angle1, side, side2)
        b2 = get_bisector(angle2, side, side1)
        r = get_inner_radius(S, P)
        return [side, side1, side2, angle, angle1, angle2, h, h1, h2, P, S, m, m1, m2, b, b1, b2, R, r]
    if angle1 or angle2:
        if angle1:
            if not legit_angle(angle1, angle):
                raise ValueError("Invalid input!")
            angle2 = get_third_angle(angle, angle1)
        else:
            if not legit_angle(angle2, angle):
                raise ValueError("Invalid input!")
            angle1 = get_third_angle(angle, angle2)
        side2 = get_side_from_2_sides(side, side1, angle2)
        P = side + side1 + side2
        S = get_surface(side, side1, side2)
        h = get_height(S, side)
        h1 = get_height(S, side1)
        m = get_median(side, side1, side2)
        m1 = get_median(side1, side, side2)
        m2 = get_median(side2, side, side1)
        b = get_bisector(angle, side1, side2)
        b1 = get_bisector(angle1, side, side2)
        b2 = get_bisector(angle2, side, side1)
        r = get_inner_radius(S, P)
        return [side, side1, side2, angle, angle1, angle2, h, h1, h2, P, S, m, m1, m2, b, b1, b2, R, r]
    if h or h1:
        if h:
            if h > side1:
                raise ValueError("Invalid input!")
            S = side * h / 2
            h1 = get_height(S, side1)
        else:
            if h1 > side:
                raise ValueError("Invalid input!")
            S = side1 * h1 / 2
            h = get_height(S, side)
        side2 = 2 * S / h2
        P = side + side1 + side2
        angle1 = get_angle_from_3_sides(side1, side, side2)
        angle2 = get_third_angle(angle, angle1)
        m = get_median(side, side1, side2)
        m1 = get_median(side1, side, side2)
        m2 = get_median(side2, side, side1)
        b = get_bisector(angle, side1, side2)
        b1 = get_bisector(angle1, side, side2)
        b2 = get_bisector(angle2, side, side1)
        r = get_inner_radius(S, P)
        return [side, side1, side2, angle, angle1, angle2, h, h1, h2, P, S, m, m1, m2, b, b1, b2, R, r]
    a_side2 = sqrt(side1 ** 2 - h2 ** 2) + sqrt(side ** 2 - h2 ** 2)
    b_side2 = sqrt(side1 ** 2 - h2 ** 2) - sqrt(side ** 2 - h2 ** 2)
    a_angle1 = get_angle_from_3_sides(side1, side, a_side2)
    b_angle1 = get_angle_from_3_sides(side1, side, b_side2)
    a_angle2 = get_third_angle(angle, a_angle1)
    b_angle2 = get_third_angle(angle, b_angle1)
    a_P = side + side1 + a_side2
    b_P = side + side1 + b_side2
    a_S = get_surface(side, side1, a_side2)
    b_S = get_surface(side, side1, b_side2)
    a_h = get_height(a_S, side)
    b_h = get_height(b_S, side)
    a_h1 = get_height(a_S, side1)
    b_h1 = get_height(b_S, side1)
    a_m = get_median(side, side1, a_side2)
    b_m = get_median(side, side1, b_side2)
    a_m1 = get_median(side1, side, a_side2)
    b_m1 = get_median(side1, side, b_side2)
    a_m2 = get_median(a_side2, side, side1)
    b_m2 = get_median(b_side2, side, side1)
    a_b = get_bisector(angle, side1, a_side2)
    b_b = get_bisector(angle, side1, b_side2)
    a_b1 = get_bisector(a_angle1, side, a_side2)
    b_b1 = get_bisector(b_angle1, side, b_side2)
    a_b2 = get_bisector(a_angle2, side, side1)
    b_b2 = get_bisector(b_angle2, side, side1)
    a_r = get_inner_radius(a_S, a_P)
    b_r = get_inner_radius(b_S, b_P)
    return [side, side1, a_side2, angle, a_angle1, a_angle2, a_h, a_h1, h2, a_P, a_S, a_m, a_m1, a_m2, a_b, a_b1, a_b2, R, a_r], [side, side1, b_side2, angle, b_angle1, b_angle2, b_h, b_h1, h2, b_P, b_S, b_m, b_m1, b_m2, b_b, b_b1, b_b2, R, b_r]


def side_angle1_height1(side, angle1, h1, h2):
    if h1 > side or angle1 >= pi / 2 and h1 >= h2:
        raise ValueError("Invalid input!")
    if angle1 < pi / 2 and h1 > h2:
        a_angle2 = get_angle_from_height_and_side(h1, side)
        b_angle2 = pi - a_angle2
        a_angle = get_third_angle(angle1, a_angle2)
        b_angle = get_third_angle(angle1, b_angle2)
        a_side1 = get_side_from_sin_theorem(side, a_angle, angle1)
        b_side1 = get_side_from_sin_theorem(side, b_angle, angle1)
        a_side2 = get_side_from_2_sides(side, a_side1, a_angle2)
        b_side2 = get_side_from_2_sides(side, b_side1, b_angle2)
        a_P = side + a_side1 + a_side2
        b_P = side + b_side1 + b_side2
        a_S = get_surface(side, a_side1, a_side2)
        b_S = get_surface(side, b_side1, b_side2)
        a_h = get_height(a_S, side)
        b_h = get_height(b_S, side)
        a_m = get_median(side, a_side1, a_side2)
        b_m = get_median(side, b_side1, b_side2)
        a_m1 = get_median(a_side1, side, a_side2)
        b_m1 = get_median(b_side1, side, b_side2)
        a_m2 = get_median(a_side2, side, a_side1)
        b_m2 = get_median(b_side2, side, b_side1)
        a_b = get_bisector(a_angle, a_side1, a_side2)
        b_b = get_bisector(b_angle, b_side1, b_side2)
        a_b1 = get_bisector(angle1, side, a_side2)
        b_b1 = get_bisector(angle1, side, b_side2)
        a_b2 = get_bisector(a_angle2, side, a_side1)
        b_b2 = get_bisector(b_angle2, side, b_side1)
        a_R = get_outer_radius(side, a_angle)
        b_R = get_outer_radius(side, b_angle)
        a_r = get_inner_radius(a_S, a_P)
        b_r = get_inner_radius(b_S, b_P)
        return [side, a_side1, a_side2, a_angle, angle1, a_angle2, a_h, h1, h2, a_P, a_S, a_m, a_m1, a_m2, a_b, a_b1, a_b2, a_R, a_r], [side, b_side1, b_side2, b_angle, angle1, b_angle2, b_h, h1, h2, b_P, b_S, b_m, b_m1, b_m2, b_b, b_b1, b_b2, b_R, b_r]
    angle2 = get_angle_from_height_and_side(h1, side)
    angle = get_third_angle(angle1, angle2)
    side1 = get_side_from_sin_theorem(side, angle, angle1)
    side2 = get_side_from_2_sides(side, side1, angle2)
    S = get_surface(side, side1, side2)
    h = get_height(S, side)
    P = side + side1 + side2
    m = get_median(side, side1, side2)
    m1 = get_median(side1, side, side2)
    m2 = get_median(side2, side, side1)
    b = get_bisector(angle, side1, side2)
    b1 = get_bisector(angle1, side, side2)
    b2 = get_bisector(angle2, side, side1)
    R = get_outer_radius(side, angle)
    r = get_inner_radius(S, P)
    return [side, side1, side2, angle, angle1, angle2, h, h1, h2, P, S, m, m1, m2, b, b1, b2, R, r]


def side_height_height1(side, h, h1, h2, S):
    if h1 > side:
        raise ValueError("Invalid input!")
    side1 = 2 * S / h1
    if h2 or h1 == side:
        if h1 == side:
            side2 = sqrt(side ** 2 + side1 ** 2)
            angle2 = pi / 2
        else:
            if h2 > min(side, side1):
                raise ValueError("Invalid input!")
            side2 = 2 * S / h2
            angle2 = get_angle_from_3_sides(side2, side, side1)
        angle = get_angle_from_3_sides(side, side1, side2)
        angle1 = get_third_angle(angle, angle2)
        P = side + side1 + side2
        m = get_median(side, side1, side2)
        m1 = get_median(side1, side, side2)
        m2 = get_median(side2, side, side1)
        b = get_bisector(angle, side1, side2)
        b1 = get_bisector(angle1, side, side2)
        b2 = get_bisector(angle2, side, side1)
        R = get_outer_radius(side, angle)
        r = get_inner_radius(S, P)
        return [side, side1, side2, angle, angle1, angle2, h, h1, h2, P, S, m, m1, m2, b, b1, b2, R, r]
    a_angle2 = get_angle_from_height_and_side(h1, side)
    b_angle2 = pi - a_angle2
    a_side2 = get_side_from_2_sides(side, side1, a_angle2)
    b_side2 = get_side_from_2_sides(side, side1, b_angle2)
    a_h2 = get_height(S, a_side2)
    b_h2 = get_height(S, b_side2)
    a_angle = get_angle_from_height_and_side(h1, a_side2)
    b_angle = get_angle_from_height_and_side(h1, b_side2)
    a_angle1 = get_third_angle(a_angle, a_angle2)
    b_angle1 = get_third_angle(b_angle, b_angle2)
    a_P = side + side1 + a_side2
    b_P = side + side1 + b_side2
    a_m = get_median(side, side1, a_side2)
    b_m = get_median(side, side1, b_side2)
    a_m1 = get_median(side1, side, a_side2)
    b_m1 = get_median(side1, side, b_side2)
    a_m2 = get_median(a_side2, side, side1)
    b_m2 = get_median(b_side2, side, side1)
    a_b = get_bisector(a_angle, side1, a_side2)
    b_b = get_bisector(b_angle, side1, b_side2)
    a_b1 = get_bisector(a_angle1, side, a_side2)
    b_b1 = get_bisector(b_angle1, side, b_side2)
    a_b2 = get_bisector(a_angle2, side, side1)
    b_b2 = get_bisector(b_angle2, side, side1)
    a_R = get_outer_radius(side, a_angle)
    b_R = get_outer_radius(side, b_angle)
    a_r = get_inner_radius(S, a_P)
    b_r = get_inner_radius(S, b_P)
    return [side, side1, a_side2, a_angle, a_angle1, a_angle2, h, h1, a_h2, a_P, S, a_m, a_m1, a_m2, a_b, a_b1, a_b2, a_R, a_r], [side, side1, b_side2, b_angle, b_angle1, b_angle2, h, h1, b_h2, b_P, S, b_m, b_m1, b_m2, b_b, b_b1, b_b2, b_R, b_r]


def given_side(side, side1, side2, angle, angle1, angle2, h, h1, h2):
    if side1:
        if side2:
            if side + side1 <= side2 or side + side2 <= side1 or side1 + side2 <= side:
                raise ValueError("Invalid input!")
            angle = get_angle_from_3_sides(side, side1, side2)
            angle1 = get_angle_from_3_sides(side1, side, side2)
            angle2 = get_angle_from_3_sides(side2, side, side1)
            S = get_surface(side, side1, side2)
            h = get_height(S, side)
            h1 = get_height(S, side1)
            h2 = get_height(S, side2)
        elif angle:
            if not legit_angle(angle):
                raise ValueError("Invalid input!")
            h2 = side1 * sin(angle)
            return side_angle_side1(side, side1, angle, angle1, angle2, h, h1, h2)
        elif angle1:
            if not legit_angle(angle1):
                raise ValueError("Invalid input!")
            h2 = side * sin(angle1)
            return rotate_right(switch_1_and_2(side_angle_side1(side1, side, angle1, angle, angle2, h1, h, h2)))
        elif angle2:
            if not legit_angle(angle2):
                raise ValueError("Invalid input!")
            side2 = get_side_from_2_sides(side, side1, angle2)
            angle = get_angle_from_3_sides(side, side1, side2)
            angle1 = get_third_angle(angle, angle2)
            S = get_surface(side, side1, side2)
            h = get_height(S, side)
            h1 = get_height(S, side1)
            h2 = get_height(S, side2)
        elif h or h1:
            if h:
                if h > side1:
                    raise ValueError("Invalid input!")
                S = side * h / 2
                h1 = get_height(S, side1)
            else:
                if h1 > side:
                    raise ValueError("Invalid input!")
                S = side1 * h1 / 2
                h = get_height(S, side)
            angle2 = get_angle_from_height_and_side(h1, side)
            side2 = get_side_from_2_sides(side, side1, angle2)
            angle = get_angle_from_height_and_side(h1, side2)
            angle1 = get_third_angle(angle, angle2)
            h2 = get_height(S, side2)
        elif h2:
            if h2 > min(side, side1):
                raise ValueError("Invalid input!")
            angle = get_angle_from_height_and_side(h2, side1)
            angle1 = get_angle_from_height_and_side(h2, side)
            angle2 = get_third_angle(angle, angle1)
            side2 = get_side_from_2_sides(side, side1, angle2)
            S = get_surface(side, side1, side2)
            h = get_height(S, side)
            h1 = get_height(S, side1)
        else:
            return [side, side1] + [0] * 17
    elif side2:
        return switch_1_and_2(given_side(side, side2, side1, angle, angle2, angle1, h, h2, h1))
    elif angle:
        R = get_outer_radius(side, angle)
        if not legit_angle(angle):
            raise ValueError("Invalid input!")
        if angle1 or angle2:
            if angle1:
                if not legit_angle(angle1, angle):
                    raise ValueError("Invalid input!")
                angle2 = get_third_angle(angle, angle1)
            else:
                if not legit_angle(angle2, angle):
                    raise ValueError("Invalid input!")
                angle1 = get_third_angle(angle, angle2)
            side1 = get_side_from_sin_theorem(side, angle, angle1)
            side2 = get_side_from_2_sides(side, side1, angle2)
            S = get_surface(side, side1, side2)
            h = get_height(S, side)
            h1 = get_height(S, side1)
            h2 = get_height(S, side2)
        elif h:
            S = side * h / 2
            if h > R + sqrt(R ** 2 - side ** 2 / 4) and angle <= pi / 2 or h > R - sqrt(R ** 2 - side ** 2 / 4) and angle > pi / 2:
                raise ValueError("Invalid input!")
            angle1 = get_angle_from_height_and_side(h, sqrt((side / 2 - sqrt(R ** 2 - (h + (-1) ** (angle < pi / 2) * sqrt(R ** 2 - side ** 2 / 4)) ** 2)) ** 2 + h ** 2))
            angle2 = get_third_angle(angle, angle1)
            side1 = get_side_from_sin_theorem(side, angle, angle1)
            side2 = get_side_from_2_sides(side, side1, angle2)
            h1 = get_height(S, side1)
            h2 = get_height(S, side2)
        elif h1:
            side2 = h1 / sin(angle)
            return switch_1_and_2(side_angle_side1(side, side2, angle, angle2, angle1, h, h2, h1))
        elif h2:
            return switch_1_and_2(given_side(side, side2, side1, angle, angle2, angle1, h, h2, h1))
        else:
            return [side, 0, 0, angle] + [0] * 13 + [get_outer_radius(side, angle), 0]
    elif angle1:
        h2 = side / sin(angle1)
        if angle2:
            if not legit_angle(angle2, angle1):
                raise ValueError("invalid input!")
            angle = get_third_angle(angle1, angle2)
            side1 = get_side_from_sin_theorem(side, angle, angle1)
            side2 = get_side_from_2_sides(side, side1, angle2)
            S = get_surface(side, side1, side2)
            h = get_height(S, side)
            h1 = get_height(S, side1)
        elif h:
            S = side * h / 2
            side2 = 2 * S / h2
            side1 = get_side_from_2_sides(side, side2, angle1)
            angle = get_angle_from_3_sides(side, side1, side2)
            angle2 = get_third_angle(angle, angle1)
            h1 = get_height(S, side1)
        elif h1:
            return side_angle1_height1(side, angle1, h1, h2)
        else:
            return [side] + [0] * 3 + [angle1] + [0] * 3 + [h2] + [0] * 10
    elif angle2:
        return switch_1_and_2(given_side(side, side2, side1, angle, angle2, angle1, h, h2, h1))
    elif h:
        S = side * h / 2
        if h1:
            return side_height_height1(side, h, h1, h2, S)
        if h2:
            return switch_1_and_2(side_height_height1(side, h, h2, h1, S))
        return [side] + [0] * 5 + [h] + [0] * 3 + [S] + [0] * 8
    elif h1:
        if h1 > side:
            raise ValueError("Invalid input!")
        angle2 = get_angle_from_height_and_side(h1, side)
        if h2:
            if h2 > side:
                raise ValueError("Invalid input!")
            if h2 > h1:
                a_angle1 = get_angle_from_height_and_side(h2, side)
                b_angle1 = pi - a_angle1
                a_angle = get_third_angle(a_angle1, angle2)
                b_angle = get_third_angle(b_angle1, angle2)
                a_side1 = get_side_from_sin_theorem(side, a_angle, a_angle1)
                b_side1 = get_side_from_sin_theorem(side, b_angle, b_angle1)
                a_side2 = get_side_from_2_sides(side, a_side1, angle2)
                b_side2 = get_side_from_2_sides(side, b_side1, angle2)
                a_S = get_surface(side, a_side1, a_side2)
                b_S = get_surface(side, b_side1, b_side2)
                a_h = get_height(a_S, side)
                b_h = get_height(b_S, side)
                a_P = side + a_side1 + a_side2
                b_P = side + b_side1 + b_side2
                a_m = get_median(side, a_side1, a_side2)
                b_m = get_median(side, b_side1, b_side2)
                a_m1 = get_median(a_side1, side, a_side2)
                b_m1 = get_median(b_side1, side, b_side2)
                a_m2 = get_median(a_side2, side, a_side1)
                b_m2 = get_median(b_side2, side, b_side1)
                a_b = get_bisector(a_angle, a_side1, a_side2)
                b_b = get_bisector(b_angle, b_side1, b_side2)
                a_b1 = get_bisector(a_angle1, side, a_side2)
                b_b1 = get_bisector(b_angle1, side, b_side2)
                a_b2 = get_bisector(angle2, side, a_side1)
                b_b2 = get_bisector(angle2, side, b_side1)
                a_R = get_outer_radius(side, a_angle)
                b_R = get_outer_radius(side, b_angle)
                a_r = get_inner_radius(a_S, a_P)
                b_r = get_inner_radius(b_S, b_P)
                return [side, a_side1, a_side2, a_angle, a_angle1, angle2, a_h, h1, h2, a_P, a_S, a_m, a_m1, a_m2, a_b, a_b1, a_b2, a_R, a_r], [side, b_side1, b_side2, b_angle, b_angle1, angle2, b_h, h1, h2, b_P, b_S, b_m, b_m1, b_m2, b_b, b_b1, b_b2, b_R, b_r]
            if h1 == h2:
                angle1 = get_angle_from_height_and_side(h2, side)
                angle = get_third_angle(angle1, angle2)
                side1 = get_side_from_sin_theorem(side, angle, angle1)
                side2 = get_side_from_2_sides(side, side1, angle2)
                S = get_surface(side, side1, side2)
                h = get_height(S, side)
            else:
                a_angle2 = angle2
                b_angle2 = pi - a_angle2
                angle1 = get_angle_from_height_and_side(h2, side)
                a_angle = get_third_angle(angle1, a_angle2)
                b_angle = get_third_angle(angle1, b_angle2)
                a_side1 = get_side_from_sin_theorem(side, a_angle, angle1)
                b_side1 = get_side_from_sin_theorem(side, b_angle, angle1)
                a_side2 = get_side_from_2_sides(side, a_side1, a_angle2)
                b_side2 = get_side_from_2_sides(side, b_side1, b_angle2)
                a_S = get_surface(side, a_side1, a_side2)
                b_S = get_surface(side, b_side1, b_side2)
                a_h = get_height(a_S, side)
                b_h = get_height(b_S, side)
                a_P = side + a_side1 + a_side2
                b_P = side + b_side1 + b_side2
                a_m = get_median(side, a_side1, a_side2)
                b_m = get_median(side, b_side1, b_side2)
                a_m1 = get_median(a_side1, side, a_side2)
                b_m1 = get_median(b_side1, side, b_side2)
                a_m2 = get_median(a_side2, side, a_side1)
                b_m2 = get_median(b_side2, side, b_side1)
                a_b = get_bisector(a_angle, a_side1, a_side2)
                b_b = get_bisector(b_angle, b_side1, b_side2)
                a_b1 = get_bisector(angle1, side, a_side2)
                b_b1 = get_bisector(angle1, side, b_side2)
                a_b2 = get_bisector(a_angle2, side, a_side1)
                b_b2 = get_bisector(b_angle2, side, b_side1)
                a_R = get_outer_radius(side, a_angle)
                b_R = get_outer_radius(side, b_angle)
                a_r = get_inner_radius(a_S, a_P)
                b_r = get_inner_radius(b_S, b_P)
                return [side, a_side1, a_side2, a_angle, angle1, a_angle2, a_h, h1, h2, a_P, a_S, a_m, a_m1, a_m2, a_b, a_b1, a_b2, a_R, a_r], [side, b_side1, b_side2, b_angle, angle1, b_angle2, b_h, h1, h2, b_P, b_S, b_m, b_m1, b_m2, b_b, b_b1, b_b2, b_R, b_r]
        else:
            return [side] + [0] * 4 + [angle2, 0, h1] + [0] * 11, [side] + [0] * 4 + [pi - angle2, 0, h1] + [0] * 11
    elif h2:
        if h2 > side:
            raise ValueError("Invalid input!")
        angle1 = get_angle_from_height_and_side(h2, side)
        return [side] + [0] * 3 + [angle1] + [0] * 3 + [h2] + [0] * 10, [side] + [0] * 3 + [pi - angle1] + [0] * 3 + [h2] + [0] * 10
    else:
        return [side] + [0] * 18
    P = side + side1 + side2
    m = get_median(side, side1, side2)
    m1 = get_median(side1, side, side2)
    m2 = get_median(side2, side, side1)
    b = get_bisector(angle, side1, side2)
    b1 = get_bisector(angle1, side, side2)
    b2 = get_bisector(angle2, side, side1)
    R = get_outer_radius(side, angle)
    r = get_inner_radius(S, P)
    return [side, side1, side2, angle, angle1, angle2, h, h1, h2, P, S, m, m1, m2, b, b1, b2, R, r]


def given_angle(angle, angle1, angle2, h, h1, h2):
    if angle1 or angle2:
        if angle1:
            if not legit_angle(angle1):
                raise ValueError("Invalid input!")
            angle2 = get_third_angle(angle, angle1)
        else:
            if not legit_angle(angle2):
                raise ValueError("Invalid input!")
            angle1 = get_third_angle(angle, angle2)
        if h:
            side1 = h / sin(angle2)
            side2 = h / sin(angle1)
            side = get_side_from_2_sides(side1, side2, angle)
            S = get_surface(side, side1, side2)
            h1 = get_height(S, side1)
            h2 = get_height(S, side2)
        elif h1:
            side = h1 / sin(angle2)
            side2 = h1 / sin(angle)
            side1 = get_side_from_2_sides(side, side2, angle1)
            S = get_surface(side, side1, side2)
            h = get_height(S, side)
            h2 = get_height(S, side2)
        elif h2:
            return switch_1_and_2(given_angle(angle, angle2, angle1, h, h2, h1))
        else:
            return [0] * 3 + [angle, angle1, angle2] + [0] * 13
    elif h:
        if h1:
            side2 = h1 / sin(angle)
            return switch_1_and_2(rotate_right(switch_1_and_2(side_angle1_height1(side2, angle, h, h1))))
        if h2:
            return switch_1_and_2(given_angle(angle, angle2, angle1, h, h2, h1))
        return [0] * 3 + [angle] + [0, 0] + [h] + [0] * 12
    elif h1:
        side2 = h1 * sin(angle)
        if h2:
            S = side2 * h2 / 2
            side1 = h2 / sin(angle)
            side = get_side_from_2_sides(side1, side2, angle)
            angle1 = get_angle_from_3_sides(side1, side, side2)
            angle2 = get_third_angle(angle, angle1)
            h = get_height(S, side)
        else:
            return [0] * 2 + [side2, angle] + [0] * 3 + [h1] + [0] * 11
    elif h2:
        return [0, h2 / sin(angle), 0, angle] + [0] * 4 + [h2] + [0] * 10
    else:
        return [0] * 3 + [angle] + [0] * 15
    P = side + side1 + side2
    m = get_median(side, side1, side2)
    m1 = get_median(side1, side, side2)
    m2 = get_median(side2, side, side1)
    b = get_bisector(angle, side1, side2)
    b1 = get_bisector(angle1, side, side2)
    b2 = get_bisector(angle2, side, side1)
    R = get_outer_radius(side, angle)
    r = get_inner_radius(S, P)
    return [side, side1, side2, angle, angle1, angle2, h, h1, h2, P, S, m, m1, m2, b, b1, b2, R, r]


def given_height(h, h1, h2):
    if h1 and h2:
        if 1 / h + 1 / h1 <= 1 / h2 or 1 / h + 1 / h2 <= 1 / h1 or 1 / h1 + 1 / h2 <= 1 / h:
            raise ValueError("Invalid input!")
        S = 1 / sqrt((1 / h + 1 / h1 + 1 / h2) * (1 / h1 - 1 / h + 1 / h2) * (1 / h - 1 / h1 + 1 / h2) * (1 / h + 1 / h1 - 1 / h2))
        side = 2 * S / h
        side1 = 2 * S / h1
        side2 = 2 * S / h2
        angle = get_angle_from_3_sides(side, side1, side2)
        angle1 = get_angle_from_3_sides(side1, side, side2)
        angle2 = get_third_angle(angle, angle1)
        P = side + side1 + side2
        m = get_median(side, side1, side2)
        m1 = get_median(side1, side, side2)
        m2 = get_median(side2, side, side1)
        b = get_bisector(angle, side1, side2)
        b1 = get_bisector(angle1, side, side2)
        b2 = get_bisector(angle2, side, side1)
        R = get_outer_radius(side, angle)
        r = get_inner_radius(S, P)
        return [side, side1, side2, angle, angle1, angle2, h, h1, h2, P, S, m, m1, m2, b, b1, b2, R, r]
    return [0] * 6 + [h, h1, h2] + [0] * 10


def get_coordinates(res_triangle: [float]):
    A_coords = (0, 0)
    B_coords = (0, 0)
    if res_triangle[2]:
        B_coords = (res_triangle[2], 0)
    C_coords = (0, 0)
    if res_triangle[3] and res_triangle[1]:
        C_coords = (sin(res_triangle[3]) * res_triangle[1], cos(res_triangle[3]) * res_triangle[1])
    coordinates = [A_coords, B_coords, C_coords, ((B_coords[0] + C_coords[0]) / 3, (B_coords[1] + C_coords[1]) / 3) if B_coords[0] + B_coords[1] and C_coords[0] + C_coords[1] else (0, 0)]
    outer_center_x, outer_center_y = 0, 0
    if res_triangle[2] and res_triangle[17]:
        angle_towards_outer_circle_center = (pi - get_angle_from_3_sides(res_triangle[2], res_triangle[17], res_triangle[17])) / 2
        outer_center_y = res_triangle[17] * sin(angle_towards_outer_circle_center)
        outer_center_x = sqrt(res_triangle[17] ** 2 - outer_center_y ** 2)
    coordinates.append((outer_center_x, outer_center_y))
    inner_radius_y = res_triangle[18]
    inner_radius_x = 0
    if res_triangle[3]:
        inner_radius_x = inner_radius_y / tan(res_triangle[3] / 2)
    coordinates.append((inner_radius_x, inner_radius_y))
    return coordinates


def calculate_triangle(a=0, b=0, c=0, A=0, B=0, C=0, h_a=0, h_b=0, h_c=0):
    A, B, C = radians(A), radians(B), radians(C)
    if a:
        res = given_side(a, b, c, A, B, C, h_a, h_b, h_c)
    elif b:
        res = rotate_right(given_side(b, c, a, B, C, A, h_b, h_c, h_a))
    elif c:
        res = rotate_right(rotate_right(given_side(c, a, b, C, A, B, h_c, h_a, h_b)))
    elif A:
        res = given_angle(A, B, C, h_a, h_b, h_c)
    elif B:
        res = rotate_right(switch_1_and_2(given_angle(B, A, C, h_b, h_a, h_c)))
    elif C:
        res = rotate_right(rotate_right(given_angle(C, A, B, h_c, h_a, h_b)))
    elif h_a:
        res = given_height(h_a, h_b, h_c)
    else:
        res = [0] * 7 + [h_b, h_c] + [0] * 10
    if len(res) == 2:
        res = (res[0] + get_coordinates(res[0]), res[1] + get_coordinates(res[1]))
        res = (res[0][:3] + list(map(degrees, res[0][3:6])) + res[0][6:], res[1][:3] + list(map(degrees, res[1][3:6])) + res[1][6:])
    else:
        res += get_coordinates(res)
        res = res[:3] + list(map(degrees, res[3:6])) + res[6:]
    return res


if __name__ == '__main__':
    Triangle = ['a', 'b', 'c', 'A', 'B', 'C', 'h_a', 'h_b', 'h_c', 'P', 'S', 'm_a', 'm_b', 'm_c', 'b_a', 'b_b', 'b_c', 'R', 'r', 'A coordinates', 'B coordinates', 'C coordinates', 'triangle center', 'outer circle center', 'inner circle center']
    values = dict(map(lambda p: (p[0].strip(), abs(float(p[1].strip()))), map(lambda x: x.split('='), input().split(', '))))
    result = calculate_triangle(**values)
    if len(result) == 2:
        print(dict(zip(Triangle, list(map(lambda x: (round(x[0], 3), round(x[1], 3)) if isinstance(x, tuple) else round(x, 3), result[0])))))
        print(dict(zip(Triangle, list(map(lambda x: (round(x[0], 3), round(x[1], 3)) if isinstance(x, tuple) else round(x, 3), result[1])))))
    else:
        print(dict(zip(Triangle, list(map(lambda x: (round(x[0], 3), round(x[1], 3)) if isinstance(x, tuple) else round(x, 3), result)))))
