from .util.vector_functions import *


def main():
    choice = int(input("Make choice: \n"
                                    "1 for shortest distance from point to plane\n"
                                    "2 for equation of plane given 3 points: "))

    if (choice == 1):
        shortest_dist_point_line_plane()
    else:
        plane_from_points()


if __name__ == "__main__":
    main()


