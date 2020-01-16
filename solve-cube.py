from Cube import Cube

def solve_cube(state):
    #TODO: Logic of cube solving
    cube = Cube(state)
    
    return

cube_sides = [
        [['W','W','W'], ['W','W','W'], ['W','W','W']],
        [['O','O','O'], ['O','O','O'], ['O','O','O']],
        [['R','R','R'], ['R','R','R'], ['R','R','R']],
        [['B','B','B'], ['B','B','B'], ['B','B','B']],
        [['Y','Y','Y'], ['Y','Y','Y'], ['Y','Y','Y']],
        [['G','G','G'], ['G','G','G'], ['G','G','G']],
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