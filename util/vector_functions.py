from cmath import acos, sqrt

# calculates magnitude of vector
def magnitude(a):
    x = 0
    sum_squares = 0
    while x < len(a):
        sum_squares += a[x] ** 2
        x += 1
    result = sqrt(sum_squares)
    return result


# calculates dot product of 2 vectors
def dot_prod(a, b):
    if len(a) != len(b):
        raise Exception("Vectors must be of the same length")

    x = 0
    result = 0
    while x < len(a):
        result += a[x] * b[x]
        x += 1
    return result


# calculates cross product of vectors a and b in R3
def cross_prod(a, b):
    result = [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]
    return result

# shortest distance between a point and a line or a plane
def shortest_dist_point_line_plane():
    point_x, point_y, point_z = [float(num) for num in input("Enter point x, y, z: ").split()]
    line_a, line_b, line_c, line_d = [float(num) for num in 
                                        input("Enter A, B, C, D in equation for line in the form Ax + By + Cz + D = 0: ").split()]

    dist = abs((line_a) * (point_x) + line_b * point_y + line_c * point_z + line_d) / sqrt(line_a ** 2 + line_b ** 2 + line_c ** 2)

    print(dist)

# find equation of plane in form ax + by + z + d = 0
def plane_from_points():
    x1, y1, z1 = [float(num) for num in input("Enter first point: ").split()]
    x2, y2, z2 = [float (num) for num in input("Enter second point: ").split()]
    x3, y3, z3 = [float (num) for num in input("Enter third point: ").split()]

    vect_a = [x2 - x1, y2 - y1, z2 - z1]
    vect_b = [x3 - x1, y3 - y1, z3 - z1]

    n = cross_prod(vect_a, vect_b)

    d = n[0] * x1 * -1 + n[1] * y1 * -1 + n[2] * z1 * -1
    print("Equation of plane is: " + str(n[0]) + "x + "
                                    + str(n[1]) + "y + "
                                    + str(n[2]) + "z + "
                                    + str(d)
                                    + " = 0")

# find angle between two planes
def angle_between_planes(n1, n2):
    cos_theta = abs(dot_prod(n1, n2)) / (magnitude(n1) * magnitude(n2))
    result = acos(cos_theta)
    return result
