class Cube:
    """
    Rubix cube representation

    The init variable sides is a 
    """
    def __init__(self, sides):
        self.sides = sides

    def rotate(self, layer, degree):
        return
    
    def rotate_front(self, degree):
        if degree == 180:
            temp_side_top = self.sides[0][2][::-1]
            temp_side_left = []
            temp_side_left.append(self.sides[1][0][2])
            temp_side_left.append(self.sides[1][1][2])
            temp_side_left.append(self.sides[1][2][2])
            temp_side_left = temp_side_left[::-1]

            print(temp_side_top)
            print(temp_side_left)

            for i in range(3):
                #Assign side values to appropriate colours

            self.sides[0][2] = self.sides[4][0][::-1]
        self.print_cube()
        return
    def rotate_back(self, degree):
        return
    def rotate_up(self, degree):
        return
    def rotate_down(self, degree):
        return
    def rotate_right(self, degree):
        return
    def rotate_left(self, degree):
        return
    def rotate_middle(self, degree):
        return
    def rotate_equator(self, degree):
        return
    def rotate_standing(self, degree):
        return
    def print_cube(self):
        print("        " + " ".join(self.sides[0][0]))
        print("        " + " ".join(self.sides[0][1]))
        print("        " + " ".join(self.sides[0][2]))

        print()

        print(" ".join(self.sides[1][0]) + "   " + " ".join(self.sides[2][0]) + "   " + " ".join(self.sides[3][0]))
        print(" ".join(self.sides[1][1]) + "   " + " ".join(self.sides[2][1]) + "   " + " ".join(self.sides[3][1]))
        print(" ".join(self.sides[1][2]) + "   " + " ".join(self.sides[2][2]) + "   " + " ".join(self.sides[3][2]))

        print()

        print("        " + " ".join(self.sides[4][0]))
        print("        " + " ".join(self.sides[4][1]))
        print("        " + " ".join(self.sides[4][2]))

        print()

        print("        " + " ".join(self.sides[5][0]))
        print("        " + " ".join(self.sides[5][1]))
        print("        " + " ".join(self.sides[5][2]))