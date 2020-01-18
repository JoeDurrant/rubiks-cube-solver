from Cube import Cube

def solve_cube(state):
    #TODO: Logic of cube solving
    cube = Cube(state)

    return

cube_sides = [
        [['W','W','W'], ['W','W','W'], ['W','W','W']],#top
        [['G','O','G'], ['G','O','G'], ['G','Y','Y']],#left
        [['R','R','B'], ['Y','G','O'], ['O','O','Y']],#front
        [['O','B','R'], ['Y','R','O'], ['R','R','B']],#right
        [['G','B','B'], ['B','Y','Y'], ['R','R','Y']],#bottom
        [['Y','B','O'], ['R','B','G'], ['O','G','B']],#back
        ]

print("        " + " ".join(cube_sides[0][0]))
print("        " + " ".join(cube_sides[0][1]))
print("        " + " ".join(cube_sides[0][2]))

print()

print(" ".join(cube_sides[1][0]) + "   " + " ".join(cube_sides[2][0]) + "   " + " ".join(cube_sides[3][0]))
print(" ".join(cube_sides[1][1]) + "   " + " ".join(cube_sides[2][1]) + "   " + " ".join(cube_sides[3][1]))
print(" ".join(cube_sides[1][2]) + "   " + " ".join(cube_sides[2][2]) + "   " + " ".join(cube_sides[3][2]))

print()

print("        " + " ".join(cube_sides[4][0]))
print("        " + " ".join(cube_sides[4][1]))
print("        " + " ".join(cube_sides[4][2]))

print()

print("        " + " ".join(cube_sides[5][0]))
print("        " + " ".join(cube_sides[5][1]))
print("        " + " ".join(cube_sides[5][2]))

cube = Cube(cube_sides)

cube.rotate_front(180)