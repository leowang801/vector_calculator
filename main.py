
from cmath import sqrt

def shortest_dist_point_line():
    point_x, point_y, point_z = [float(num) for num in input("Enter point x, y, z: ").split()]
    line_a, line_b, line_c, line_d = [float(num) for num in 
                                        input("Enter A, B, C, D in equation for line in the form Ax + By + Cz + D = 0: ").split()]

    dist = abs((line_a) * (point_x) + line_b * point_y + line_c * point_z + line_d) / sqrt(line_a ** 2 + line_b ** 2 + line_c ** 2)

    print(dist)

def cross_prod(a, b):
    result = [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]
    return result

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

def main():
    choice = int(input("Make choice: \n"
                                    "1 for shortest distance from point to plane\n"
                                    "2 for equation of plane given 3 points: "))

    if (choice == 1):
        shortest_dist_point_line()
    else:
        plane_from_points()


main()


