# Imports
import math

# Classes


class Vector:
    def __init__(self, direction, magnitude, degree):
        self.direction = direction
        self.magnitude = magnitude
        self.degree = degree


# Function
def adding_forces(force_sum, force1, force2):
    # Vector reversal if first direction is an X value
    if force_sum.direction[0] == 'W' or force_sum.direction[0] == 'E':
        if int(force_sum.degree) < 90:
            sum_y = force_sum.direction[0]
            sum_x = force_sum.direction[1]
            force_sum.direction = sum_x + sum_y
            force_sum.degree = 90 - int(force_sum.degree)
        elif 90 < int(force_sum.degree) < 180:
            sum_y = force_sum.direction[0]
            sum_x = force_sum.direction[1]
            if sum_y == 'W':
                sum_y = 'E'
            elif sum_y == 'E':
                sum_y = 'W'
            force_sum.direction = sum_x + sum_y
            force_sum.degree = int(force_sum.degree) - 90
    if force1.direction[0] == 'W' or force1.direction[0] == 'E':
        if int(force1.degree) < 90:
            sum_y = force1.direction[0]
            sum_x = force1.direction[1]
            force1.direction = sum_x + sum_y
            force1.degree = 90 - int(force1.degree)
        elif 90 < int(force1.degree) < 180:
            sum_y = force1.direction[0]
            sum_x = force1.direction[1]
            if sum_y == 'W':
                sum_y = 'E'
            elif sum_y == 'E':
                sum_y = 'W'
            force1.direction = sum_x + sum_y
            force1.degree = int(force1.degree) - 90
    if force2.direction[0] == 'W' or force2.direction[0] == 'E':
        if int(force2.degree) < 90:
            sum_y = force2.direction[0]
            sum_x = force2.direction[1]
            force2.direction = sum_x + sum_y
            force2.degree = 90 - int(force2.degree)
        elif 90 < int(force2.degree) < 180:
            sum_y = force2.direction[0]
            sum_x = force2.direction[1]
            if sum_y == 'W':
                sum_y = 'E'
            elif sum_y == 'E':
                sum_y = 'W'
            force2.direction = sum_x + sum_y
            force2.degree = int(force2.degree) - 90
    # Solving for values
    if force_sum.direction and force_sum.magnitude and force_sum.degree == '?':
        force1.magnitude = float(force1.magnitude)
        force1.degree = float(force1.degree)
        force2.magnitude = float(force2.magnitude)
        force2.degree = float(force2.degree)
        if force1.direction == 'N' and force2.direction == 'S' or force1.direction == 'S' and force2.direction == 'N':
            if force1.magnitude >= force2.magnitude:
                force_sum.direction = force1.direction
                force_sum.magnitude = force1.magnitude - force2.magnitude
                return "Force sum is: " + str(force_sum.magnitude) + "N[" + force_sum.direction + "]"
            elif force2.magnitude > force1.magnitude:
                force_sum.direction = force2.direction
                force_sum.magnitude = force2.magnitude - force1.magnitude
                return "Force sum is: " + str(force_sum.magnitude) + "N[" + force_sum.direction + "]"
        elif force1.direction == 'N' and force2.direction == 'N':
            force_sum.direction = 'N'
            force_sum.magnitude = force1.magnitude + force2.magnitude
            return "Force sum is: " + str(force_sum.magnitude) + "N[" + force_sum.direction + "]"
        elif force1.direction == 'S' and force2.direction == 'S':
            force_sum.direction = 'S'
            force_sum.magnitude = force1.magnitude + force2.magnitude
            return "Force sum is: " + str(force_sum.magnitude) + "N[" + force_sum.direction + "]"
        elif force1.direction == 'W' and force2.direction == 'W' or force1.direction == 'E' and force2.direction == 'E':
            force_sum.direction = force1.direction
            force_sum.magnitude = force1.magnitude + force2.magnitude
            return "Force sum is: " + str(force_sum.magnitude) + "N[" + force_sum.direction + "]"
        elif force1.direction == 'W' and force2.direction == 'E' or force1.direction == 'E' and force2.direction == 'W':
            if force1.magnitude >= force2.magnitude:
                force_sum.direction = force1.direction
                force_sum.magnitude = force1.magnitude - force2.magnitude
                return "Force sum is: " + str(force_sum.magnitude) + "N[" + force_sum.direction + "]"
            elif force2.magnitude > force1.magnitude:
                force_sum.direction = force2.direction
                force_sum.magnitude = force2.magnitude - force1.magnitude
                return "Force sum is: " + str(force_sum.magnitude) + "N[" + force_sum.direction + "]"
        elif (force1.direction == "N" or force1.direction == 'S' or force1.direction == 'W' or force1.direction == 'E') and (force2.direction == 'N' or force2.direction == 'S' or force2.direction == 'W' or force2.direction == "E") and force1.direction != force2.direction and not(force1.direction == 'W' and force2.direction == 'E') and not(force1.direction == 'E' and force2.direction == 'W') and not(force1.direction == 'N' and force2.direction == 'S') and not(force1.direction == 'S' and force2.direction == 'N'):
            if force1.direction == 'N' or force1.direction == 'S':
                force_sum.direction = force1.direction + force2.direction
                force_sum.magnitude = math.sqrt(force1.magnitude ** 2 + force2.magnitude ** 2)
                force_sum.degree = round(math.degrees(math.atan(force2.magnitude / force1.magnitude)), 1)
                return "Force sum is: " + str(force_sum.magnitude) + "N[" + str(force1.direction) + str(force_sum.degree) + str(force2.direction) + "]"
            elif force2.direction == 'N' or force2.direction == 'S':
                force_sum.direction = force2.direction + force1.direction
                force_sum.magnitude = math.sqrt(force1.magnitude ** 2 + force2.magnitude ** 2)
                force_sum.degree = round(math.degrees(math.atan(force1.magnitude / force2.magnitude)), 1)
                return "Force sum is: " + str(force_sum.magnitude) + "N[" + str(force2.direction) + str(force_sum.degree) + str(force1.direction) + "]"
        elif force1.degree != 0 and force2.degree != 0:
            x1 = Vector(force1.direction[1], force1.magnitude * math.sin(math.radians(force1.degree)), 0)
            y1 = Vector(force1.direction[0], force1.magnitude * math.cos(math.radians(force1.degree)), 0)
            x2 = Vector(force2.direction[1], force2.magnitude * math.sin(math.radians(force2.degree)), 0)
            y2 = Vector(force2.direction[0], force2.magnitude * math.cos(math.radians(force2.degree)), 0)
            if x1.direction == x2.direction:
                xsum = Vector(x1.direction, x1.magnitude + x2.magnitude, 0)
            else:
                if x1.magnitude >= x2.magnitude:
                    xsum = Vector(x1.direction, x1.magnitude - x2.magnitude, 0)
                else:
                    xsum = Vector(x2.direction, x2.magnitude - x1.magnitude, 0)
            if y1.direction == y2.direction:
                ysum = Vector(y1.direction, y1.magnitude + y2.magnitude, 0)
            else:
                if y1.magnitude >= y2.magnitude:
                    ysum = Vector(y1.direction, y1.magnitude - y2.magnitude, 0)
                else:
                    ysum = Vector(y2.direction, y2.magnitude - y1.magnitude, 0)
            force_sum.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
            force_sum.direction = ysum.direction + xsum.direction
            force_sum.degree = round(math.degrees(math.atan(xsum.magnitude / ysum.magnitude)), 1)
            return "Force sum is equal to: " + str(force_sum.magnitude) + "N[" + str(force_sum.direction[0]) + str(force_sum.degree) + str(force_sum.direction[1]) + "]"
        elif force1.degree != 0 and force2.degree == 0 or force1.degree == 0 and force2.degree != 0:
            if len(force1.direction) == 2:
                x1 = Vector(force1.direction[1], force1.magnitude * math.sin(math.radians(force1.degree)), 0)
                y1 = Vector(force1.direction[0], force1.magnitude * math.cos(math.radians(force1.degree)), 0)
                if force2.direction == 'W' or force2.direction == 'E':
                    ysum = y1
                    if x1.direction == force2.direction:
                        xsum = Vector(x1.direction, x1.magnitude + force2.magnitude, 0)
                    else:
                        if x1.magnitude >= force2.magnitude:
                            xsum = Vector(x1.direction, x1.magnitude - force2.magnitude, 0)
                        else:
                            xsum = Vector(force2.direction, force2.magnitude - x1.magnitude, 0)
                    force_sum.direction = ysum.direction + xsum.direction
                    force_sum.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force_sum.degree = round(math.degrees(math.atan(xsum.magnitude / ysum.magnitude)), 1)
                    return "Force sum is equal to: " + str(force_sum.magnitude) + "N[" + str(force_sum.direction[0]) + str(force_sum.degree) + str(force_sum.direction[1]) + "]"
                elif force2.direction == 'N' or force2.direction == 'S':
                    xsum = x1
                    if y1.direction == force2.direction:
                        ysum = Vector(y1.direction, y1.magnitude + force2.magnitude, 0)
                    else:
                        if y1.magnitude >= force2.magnitude:
                            ysum = Vector(y1.direction, y1.magnitude - force2.magnitude, 0)
                        else:
                            ysum = Vector(force2.direction, force2.magnitude - y1.magnitude, 0)
                    force_sum.direction = ysum.direction + xsum.direction
                    force_sum.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force_sum.degree = round(math.degrees(math.atan(xsum.magnitude / ysum.magnitude)), 1)
                    return "Force sum is equal to: " + str(force_sum.magnitude) + "N[" + str(force_sum.direction[0]) + str(force_sum.degree) + str(force_sum.direction[1]) + "]"
                else:
                    return "Invalid input."
            elif len(force2.direction) == 2:
                x1 = Vector(force2.direction[1], force2.magnitude * math.cos(math.radians(force2.degree)), 0)
                y1 = Vector(force2.direction[0], force2.magnitude * math.sin(math.radians(force2.degree)), 0)
                if force1.direction == 'E' or force1.direction == 'W':
                    ysum = y1
                    if x1.direction == force1.direction:
                        xsum = Vector(x1.direction, x1.magnitude + force1.magnitude, 0)
                    else:
                        if x1.magnitude >= force1.magnitude:
                            xsum = Vector(x1.direction, x1.magnitude - force1.magnitude, 0)
                        else:
                            xsum = Vector(force1.direction, force1.magnitude - x1.magnitude, 0)
                    force_sum.direction = ysum.direction + xsum.direction
                    force_sum.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force_sum.degree = round(math.degrees(math.atan(xsum.magnitude / ysum.magnitude)), 1)
                    return "Force sum is equal to: " + str(force_sum.magnitude) + "N[" + str(force_sum.direction[0]) + str(force_sum.degree) + str(force_sum.direction[1]) + "]"
                elif force1.direction == 'N' or force1.direction == 'S':
                    xsum = x1
                    if y1.direction == force1.direction:
                        ysum = Vector(y1.direction, y1.magnitude + force1.magnitude, 0)
                    else:
                        if y1.magnitude >= force1.magnitude:
                            ysum = Vector(y1.direction, y1.magnitude - force1.magnitude, 0)
                        else:
                            ysum = Vector(force1.direction, force1.magnitude - y1.magnitude, 0)
                    force_sum.direction = ysum.direction + xsum.direction
                    force_sum.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force_sum.degree = round(math.degrees(math.atan(xsum.magnitude / ysum.magnitude)), 1)
                    return "Force sum is equal to: " + str(force_sum.magnitude) + "N[" + str(force_sum.direction[0]) + str(force_sum.degree) + str(force_sum.direction[1]) + "]"
                else:
                    return "Invalid input."
        else:
            return "Invalid input."
    elif force1.direction and force1.magnitude and force1.degree == '?':
        force_sum.magnitude = float(force_sum.magnitude)
        force_sum.degree = float(force_sum.degree)
        force2.magnitude = float(force2.magnitude)
        force2.degree = float(force2.degree)
        if force_sum.direction == force2.direction and force_sum.degree == 0 and force2.degree == 0:
            force1.magnitude = force_sum.magnitude - force2.magnitude
            if force1.magnitude < 0:
                force1.magnitude = abs(force1.magnitude)
                if force2.direction == "N":
                    force1.direction = 'S'
                elif force2.direction == 'S':
                    force1.direction = 'N'
                elif force2.direction == 'W':
                    force1.direction = 'E'
                elif force2.direction == 'E':
                    force1.direction = 'W'
                return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction) + "]"
            elif force1.magnitude >= 0:
                force1.direction = force_sum.direction
                return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction) + "]"
        elif force_sum.direction == 'N' and force2.direction == 'S' or force_sum.direction == 'S' and force2.direction == 'N' or force_sum.direction == 'W' and force2.direction == 'E' or force_sum.direction == 'E' and force2.direction == 'W' and force_sum.degree == 0 and force2.degree == 0:
            if force_sum.magnitude >= force2.magnitude:
                force1.direction = force_sum.direction
                force1.magnitude = force_sum.magnitude - force2.magnitude
                return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction) + "]"
            elif force2.magnitude > force_sum.magnitude:
                force1.direction = force2.direction
                force1.magnitude = force2.magnitude - force_sum.magnitude
                return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction) + "]"
        elif (force_sum.direction == 'N' or force_sum.direction == 'S' or force_sum.direction == 'E' or force_sum.direction == 'W') and (force2.direction == 'N' or force2.direction == 'S' or force2.direction == 'E' or force2.direction == 'W') and (force_sum.direction != force2.direction) and not(force_sum.direction == 'W' and force2.direction == 'E') and not(force_sum.direction == 'E' and force2.direction == 'W') and not(force_sum.direction == 'N' and force2.direction == 'S') and not(force_sum.direction == 'S' and force2.direction == 'N') and force_sum.degree == 0 and force2.degree == 0:
            if force_sum.direction == 'N' or force_sum.direction == 'S':
                if force2.direction == 'W':
                    force2.direction = 'E'
                    force1.magnitude = math.sqrt(force_sum.magnitude ** 2 + force2.magnitude ** 2)
                    force1.direction = force_sum.direction + force2.direction
                    force1.degree = round(math.degrees(math.atan(force2.magnitude / force_sum.magnitude)))
                    return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction) + str(force1.degree) + "]"
                elif force2.direction == 'E':
                    force2.direction = 'W'
                    force1.magnitude = math.sqrt(force_sum.magnitude ** 2 + force2.magnitude ** 2)
                    force1.direction = force_sum.direction + force2.direction
                    force1.degree = round(math.degrees(math.atan(force2.magnitude / force_sum.magnitude)))
                    return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction) + str(force1.degree) + "]"
            elif force2.direction == 'N' or force2.direction == 'S':
                if force_sum.direction == 'W':
                    force_sum.direction = 'E'
                    force1.magnitude = math.sqrt(force2.magnitude ** 2 + force_sum.magnitude ** 2)
                    force1.direction = force2.direction + force_sum.direction
                    force1.degree = round(math.degrees(math.atan(force_sum.magnitude / force2.magnitude)))
                    return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction) + str(force1.degree) + "]"
                elif force_sum.direction == 'E':
                    force_sum.direction = 'W'
                    force1.magnitude = math.sqrt(force2.magnitude ** 2 + force_sum.magnitude ** 2)
                    force1.direction = force2.direction + force_sum.direction
                    force1.degree = round(math.degrees(math.atan(force_sum.magnitude / force2.magnitude)))
                    return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction) + str(force1.degree) + "]"
        elif force_sum.degree != 0 and force2.degree != 0:
            force2.direction = list(force2.direction)
            if force2.direction[0] == 'N':
                force2.direction[0] = 'S'
            elif force2.direction[0] == 'S':
                force2.direction[0] = 'N'
            elif force2.direction[0] == 'W':
                force2.direction[0] = 'E'
            elif force2.direction[0] == 'E':
                force2.direction[0] = 'W'
            if force2.direction[1] == 'N':
                force2.direction[1] = 'S'
            elif force2.direction[1] == 'S':
                force2.direction[1] = 'N'
            elif force2.direction[1] == 'W':
                force2.direction[1] = 'E'
            elif force2.direction[1] == 'E':
                force2.direction[1] = 'W'
            force2.direction = str(force2.direction[0] + force2.direction[1])
            x1 = Vector(force_sum.direction[1], force_sum.magnitude * math.sin(math.radians(force_sum.degree)), 0)
            y1 = Vector(force_sum.direction[0], force_sum.magnitude * math.cos(math.radians(force_sum.degree)), 0)
            x2 = Vector(force2.direction[1], force2.magnitude * math.sin(math.radians(force2.degree)), 0)
            y2 = Vector(force2.direction[0], force2.magnitude * math.cos(math.radians(force2.degree)), 0)
            if x1.direction == x2.direction:
                xsum = Vector(x1.direction, x1.magnitude + x2.magnitude, 0)
            else:
                if x1.magnitude >= x2.magnitude:
                    xsum = Vector(x1.direction, x1.magnitude - x2.magnitude, 0)
                else:
                    xsum = Vector(x2.direction, x2.magnitude - x1.magnitude, 0)
            if y1.direction == y2.direction:
                ysum = Vector(y1.direction, y1.magnitude + y2.magnitude, 0)
            else:
                if y1.magnitude >= y2.magnitude:
                    ysum = Vector(y1.direction, y1.magnitude - y2.magnitude, 0)
                else:
                    ysum = Vector(y2.direction, y2.magnitude - y1.magnitude, 0)
            force1.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
            force1.direction = ysum.direction + xsum.direction
            force1.degree = round(math.degrees(math.atan(xsum.magnitude / ysum.magnitude)), 1)
            return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction[0]) + str(force1.degree) + str(force1.direction[1]) + "]"
        elif force_sum.degree != 0 and force2.degree == 0 or force_sum.degree == 0 and force2.degree != 0:
            if len(force_sum.direction) == 2:
                force2.direction = list(force2.direction)
                if force2.direction[0] == 'N':
                    force2.direction[0] = 'S'
                elif force2.direction[0] == 'S':
                    force2.direction[0] = 'N'
                elif force2.direction[0] == 'W':
                    force2.direction[0] = 'E'
                elif force2.direction[0] == 'E':
                    force2.direction[0] = 'W'
                else:
                    return "Invalid input."
                force2.direction = str(force2.direction[0])
                x1 = Vector(force_sum.direction[1], force_sum.magnitude * math.sin(math.radians(force_sum.degree)), 0)
                y1 = Vector(force_sum.direction[0], force_sum.magnitude * math.cos(math.radians(force_sum.degree)), 0)
                if force2.direction == 'E' or force2.direction == 'W':
                    ysum = y1
                    if x1.direction == force2.direction:
                        xsum = Vector(x1.direction, x1.magnitude + force2.magnitude, 0)
                    else:
                        if x1.magnitude >= force2.magnitude:
                            xsum = Vector(x1.direction, x1.magnitude - force2.magnitude, 0)
                        else:
                            xsum = Vector(force2.direction, force2.magnitude - x1.magnitude, 0)
                    force1.direction = ysum.direction + xsum.direction
                    force1.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force1.degree = round(math.degrees(math.atan(ysum.magnitude / xsum.magnitude)), 1)
                    return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction[0]) + str(force1.degree) + str(force1.direction[1]) + "]"
                elif force2.direction == 'S' or force2.direction == 'N':
                    xsum = x1
                    if y1.direction == force2.direction:
                        ysum = Vector(y1.direction, y1.magnitude + force2.magnitude, 0)
                    else:
                        if y1.magnitude >= force2.magnitude:
                            ysum = Vector(y1.direction, y1.magnitude - force2.magnitude, 0)
                        else:
                            ysum = Vector(force2.direction, force2.magnitude - y1.magnitude, 0)
                    force1.direction = ysum.direction + xsum.direction
                    force1.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force1.degree = round(math.degrees(math.atan(ysum.magnitude / xsum.magnitude)), 1)
                    return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction[0]) + str(force1.degree) + str(force1.direction[1]) + "]"
                else:
                    return "Invalid input."
            elif len(force2.direction) == 2:
                force2.direction = list(force2.direction)
                if force2.direction[0] == 'N':
                    force2.direction[0] = 'S'
                elif force2.direction[0] == 'S':
                    force2.direction[0] = 'N'
                elif force2.direction[0] == 'W':
                    force2.direction[0] = 'E'
                elif force2.direction[0] == 'E':
                    force2.direction[0] = 'W'
                if force2.direction[1] == 'N':
                    force2.direction[1] = 'S'
                elif force2.direction[1] == 'S':
                    force2.direction[1] = 'N'
                elif force2.direction[1] == 'W':
                    force2.direction[1] = 'E'
                elif force2.direction[1] == 'E':
                    force2.direction[1] = 'W'
                force2.direction = str(force2.direction[0] + force2.direction[1])
                x1 = Vector(force2.direction[1], force2.magnitude * math.sin(math.radians(force2.degree)), 0)
                y1 = Vector(force2.direction[0], force2.magnitude * math.cos(math.radians(force2.degree)), 0)
                if force_sum.direction == 'E' or force_sum.direction == 'W':
                    ysum = y1
                    if x1.direction == force_sum.direction:
                        xsum = Vector(x1.direction, x1.magnitude + force_sum.magnitude, 0)
                    else:
                        if x1.magnitude >= force_sum.magnitude:
                            xsum = Vector(x1.direction, x1.magnitude - force_sum.magnitude, 0)
                        else:
                            xsum = Vector(force_sum.direction, force_sum.magnitude - x1.magnitude, 0)
                    force1.direction = ysum.direction + xsum.direction
                    force1.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force1.degree = round(math.degrees(math.atan(ysum.magnitude / xsum.magnitude)), 1)
                    return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction[0]) + str(force1.degree) + str(force1.direction[1]) + "]"
                elif force_sum.direction == 'S' or force_sum.direction == 'N':
                    xsum = x1
                    if y1.direction == force_sum.direction:
                        ysum = Vector(y1.direction, y1.magnitude + force_sum.magnitude, 0)
                    else:
                        if y1.magnitude >= force_sum.magnitude:
                            ysum = Vector(y1.direction, y1.magnitude - force_sum.magnitude, 0)
                        else:
                            ysum = Vector(force_sum.direction, force_sum.magnitude - y1.magnitude, 0)
                    force1.direction = ysum.direction + xsum.direction
                    force1.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force1.degree = round(math.degrees(math.atan(ysum.magnitude / xsum.magnitude)), 1)
                    return "Force one is equal to: " + str(force1.magnitude) + "N[" + str(force1.direction[0]) + str(force1.degree) + str(force1.direction[1]) + "]"
                else:
                    return "Invalid input."
    elif force2.direction and force2.magnitude and force2.degree == '?':
        force_sum.magnitude = float(force_sum.magnitude)
        force_sum.degree = float(force_sum.degree)
        force1.magnitude = float(force1.magnitude)
        force1.degree = float(force1.degree)
        if force_sum.direction == force1.direction and force_sum.degree == 0 and force1.degree == 0:
            force2.magnitude = force_sum.magnitude - force1.magnitude
            if force2.magnitude < 0:
                force2.magnitude = abs(force2.magnitude)
                if force1.direction == "N":
                    force2.direction = 'S'
                elif force1.direction == 'S':
                    force2.direction = 'N'
                elif force1.direction == 'W':
                    force2.direction = 'E'
                elif force1.direction == 'E':
                    force2.direction = 'W'
                return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction) + "]"
            elif force2.magnitude >= 0:
                force2.direction = force_sum.direction
                return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction) + "]"
        elif force_sum.direction == 'N' and force1.direction == 'S' or force_sum.direction == 'S' and force1.direction == 'N' or force_sum.direction == 'W' and force1.direction == 'E' or force_sum.direction == 'E' and force1.direction == 'W' and force_sum.degree == 0 and force1.degree == 0:
            if force_sum.magnitude >= force1.magnitude:
                force2.direction = force_sum.direction
                force2.magnitude = force_sum.magnitude - force1.magnitude
                return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction) + "]"
            elif force1.magnitude > force_sum.magnitude:
                force2.direction = force1.direction
                force2.magnitude = force1.magnitude - force_sum.magnitude
                return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction) + "]"
        elif (force_sum.direction == 'N' or force_sum.direction == 'S' or force_sum.direction == 'E' or force_sum.direction == 'W') and (force1.direction == 'N' or force1.direction == 'S' or force1.direction == 'E' or force1.direction == 'W') and (force_sum.direction != force1.direction) and not(force_sum.direction == 'W' and force1.direction == 'E') and not(force_sum.direction == 'E' and force1.direction == 'W') and not(force_sum.direction == 'N' and force1.direction == 'S') and not(force_sum.direction == 'S' and force1.direction == 'N') and force_sum.degree == 0 and force1.degree == 0:
            if force_sum.direction == 'N' or force_sum.direction == 'S':
                if force1.direction == 'W':
                    force1.direction = 'E'
                    force2.magnitude = math.sqrt(force_sum.magnitude ** 2 + force1.magnitude ** 2)
                    force2.direction = force_sum.direction + force1.direction
                    force2.degree = round(math.degrees(math.atan(force1.magnitude / force_sum.magnitude)))
                    return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction) + str(force2.degree) + "]"
                elif force1.direction == 'E':
                    force1.direction = 'W'
                    force2.magnitude = math.sqrt(force_sum.magnitude ** 2 + force1.magnitude ** 2)
                    force2.direction = force_sum.direction + force1.direction
                    force2.degree = round(math.degrees(math.atan(force1.magnitude / force_sum.magnitude)))
                    return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction) + str(force2.degree) + "]"
            elif force1.direction == 'N' or force1.direction == 'S':
                if force_sum.direction == 'W':
                    force_sum.direction = 'E'
                    force2.magnitude = math.sqrt(force1.magnitude ** 2 + force_sum.magnitude ** 2)
                    force2.direction = force1.direction + force_sum.direction
                    force2.degree = round(math.degrees(math.atan(force_sum.magnitude / force1.magnitude)))
                    return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction) + str(force2.degree) + "]"
                elif force_sum.direction == 'E':
                    force_sum.direction = 'W'
                    force2.magnitude = math.sqrt(force1.magnitude ** 2 + force_sum.magnitude ** 2)
                    force2.direction = force1.direction + force_sum.direction
                    force2.degree = round(math.degrees(math.atan(force_sum.magnitude / force1.magnitude)))
                    return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction) + str(force2.degree) + "]"
        elif force_sum.degree != 0 and force1.degree != 0:
            force1.direction = list(force1.direction)
            if force1.direction[0] == 'N':
                force1.direction[0] = 'S'
            elif force1.direction[0] == 'S':
                force1.direction[0] = 'N'
            elif force1.direction[0] == 'W':
                force1.direction[0] = 'E'
            elif force1.direction[0] == 'E':
                force1.direction[0] = 'W'
            if force1.direction[1] == 'N':
                force1.direction[1] = 'S'
            elif force1.direction[1] == 'S':
                force1.direction[1] = 'N'
            elif force1.direction[1] == 'W':
                force1.direction[1] = 'E'
            elif force1.direction[1] == 'E':
                force1.direction[1] = 'W'
            force1.direction = str(force1.direction[0] + force1.direction[1])
            x1 = Vector(force_sum.direction[1], force_sum.magnitude * math.sin(math.radians(force_sum.degree)), 0)
            y1 = Vector(force_sum.direction[0], force_sum.magnitude * math.cos(math.radians(force_sum.degree)), 0)
            x2 = Vector(force1.direction[1], force1.magnitude * math.sin(math.radians(force1.degree)), 0)
            y2 = Vector(force1.direction[0], force1.magnitude * math.cos(math.radians(force1.degree)), 0)
            if x1.direction == x2.direction:
                xsum = Vector(x1.direction, x1.magnitude + x2.magnitude, 0)
            else:
                if x1.magnitude >= x2.magnitude:
                    xsum = Vector(x1.direction, x1.magnitude - x2.magnitude, 0)
                else:
                    xsum = Vector(x2.direction, x2.magnitude - x1.magnitude, 0)
            if y1.direction == y2.direction:
                ysum = Vector(y1.direction, y1.magnitude + y2.magnitude, 0)
            else:
                if y1.magnitude >= y2.magnitude:
                    ysum = Vector(y1.direction, y1.magnitude - y2.magnitude, 0)
                else:
                    ysum = Vector(y2.direction, y2.magnitude - y1.magnitude, 0)
            force2.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
            force2.direction = ysum.direction + xsum.direction
            force2.degree = round(math.degrees(math.atan(xsum.magnitude / ysum.magnitude)), 1)
            return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction[0]) + str(force2.degree) + str(force2.direction[1]) + "]"
        elif force_sum.degree != 0 and force1.degree == 0 or force_sum.degree == 0 and force1.degree != 0:
            if len(force_sum.direction) == 2:
                force1.direction = list(force1.direction)
                if force1.direction[0] == 'N':
                    force1.direction[0] = 'S'
                elif force1.direction[0] == 'S':
                    force1.direction[0] = 'N'
                elif force1.direction[0] == 'W':
                    force1.direction[0] = 'E'
                elif force1.direction[0] == 'E':
                    force1.direction[0] = 'W'
                else:
                    return "Invalid input."
                force1.direction = str(force1.direction[0])
                x1 = Vector(force_sum.direction[1], force_sum.magnitude * math.sin(math.radians(force_sum.degree)), 0)
                y1 = Vector(force_sum.direction[0], force_sum.magnitude * math.cos(math.radians(force_sum.degree)), 0)
                if force1.direction == 'E' or force1.direction == 'W':
                    ysum = y1
                    if x1.direction == force1.direction:
                        xsum = Vector(x1.direction, x1.magnitude + force1.magnitude, 0)
                    else:
                        if x1.magnitude >= force1.magnitude:
                            xsum = Vector(x1.direction, x1.magnitude - force1.magnitude, 0)
                        else:
                            xsum = Vector(force1.direction, force1.magnitude - x1.magnitude, 0)
                    force2.direction = ysum.direction + xsum.direction
                    force2.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force2.degree = round(math.degrees(math.atan(ysum.magnitude / xsum.magnitude)), 1)
                    return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction[0]) + str(force2.degree) + str(force2.direction[1]) + "]"
                elif force1.direction == 'S' or force1.direction == 'N':
                    xsum = x1
                    if y1.direction == force1.direction:
                        ysum = Vector(y1.direction, y1.magnitude + force1.magnitude, 0)
                    else:
                        if y1.magnitude >= force1.magnitude:
                            ysum = Vector(y1.direction, y1.magnitude - force1.magnitude, 0)
                        else:
                            ysum = Vector(force1.direction, force1.magnitude - y1.magnitude, 0)
                    force2.direction = ysum.direction + xsum.direction
                    force2.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force2.degree = round(math.degrees(math.atan(ysum.magnitude / xsum.magnitude)), 1)
                    return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction[0]) + str(force2.degree) + str(force2.direction[1]) + "]"
                else:
                    return "Invalid input."
            elif len(force1.direction) == 2:
                force1.direction = list(force1.direction)
                if force1.direction[0] == 'N':
                    force1.direction[0] = 'S'
                elif force1.direction[0] == 'S':
                    force1.direction[0] = 'N'
                elif force1.direction[0] == 'W':
                    force1.direction[0] = 'E'
                elif force1.direction[0] == 'E':
                    force1.direction[0] = 'W'
                if force1.direction[1] == 'N':
                    force1.direction[1] = 'S'
                elif force1.direction[1] == 'S':
                    force1.direction[1] = 'N'
                elif force1.direction[1] == 'W':
                    force1.direction[1] = 'E'
                elif force1.direction[1] == 'E':
                    force1.direction[1] = 'W'
                force1.direction = str(force1.direction[0] + force1.direction[1])
                x1 = Vector(force1.direction[1], force1.magnitude * math.sin(math.radians(force1.degree)), 0)
                y1 = Vector(force1.direction[0], force1.magnitude * math.cos(math.radians(force1.degree)), 0)
                if force_sum.direction == 'E' or force_sum.direction == 'W':
                    ysum = y1
                    if x1.direction == force_sum.direction:
                        xsum = Vector(x1.direction, x1.magnitude + force_sum.magnitude, 0)
                    else:
                        if x1.magnitude >= force_sum.magnitude:
                            xsum = Vector(x1.direction, x1.magnitude - force_sum.magnitude, 0)
                        else:
                            xsum = Vector(force_sum.direction, force_sum.magnitude - x1.magnitude, 0)
                    force2.direction = ysum.direction + xsum.direction
                    force2.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force2.degree = round(math.degrees(math.atan(ysum.magnitude / xsum.magnitude)), 1)
                    return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction[0]) + str(force2.degree) + str(force2.direction[1]) + "]"
                elif force_sum.direction == 'S' or force_sum.direction == 'N':
                    xsum = x1
                    if y1.direction == force_sum.direction:
                        ysum = Vector(y1.direction, y1.magnitude + force_sum.magnitude, 0)
                    else:
                        if y1.magnitude >= force_sum.magnitude:
                            ysum = Vector(y1.direction, y1.magnitude - force_sum.magnitude, 0)
                        else:
                            ysum = Vector(force_sum.direction, force_sum.magnitude - y1.magnitude, 0)
                    force2.direction = ysum.direction + xsum.direction
                    force2.magnitude = math.sqrt(xsum.magnitude ** 2 + ysum.magnitude ** 2)
                    force2.degree = round(math.degrees(math.atan(ysum.magnitude / xsum.magnitude)), 1)
                    return "Force two is equal to: " + str(force2.magnitude) + "N[" + str(force2.direction[0]) + str(force2.degree) + str(force2.direction[1]) + "]"
                else:
                    return "Invalid input."
    # Invalid input
    else:
        return "Invalid input."
