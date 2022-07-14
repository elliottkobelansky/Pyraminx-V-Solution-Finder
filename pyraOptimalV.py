import numpy as np
import copy

perm = [0, 1, 2, 3, 4, 5] # UL RU LB FD RD LD
orient = [0, 0, 0, 0, 0, 0] # orientation of each edge
centers = [0, 0, 0, 0] # 0 for solved, 1 after a cw twist, 2 after a ccw twist; URLB
scramble = input().split()
for _ in scramble:
    if _ == 'U':
        perm[0], perm[1], perm[2] = perm[1], perm[2], perm[0]
        centers[0] = (centers[0] + 1) % 3
        orient[0], orient[1], orient[2] = orient[1], orient[2], orient[0]
    elif _ == "U'":
        perm[0], perm[1], perm[2] = perm[2], perm[0], perm[1]
        centers[0] = (centers[0] - 1) % 3
        orient[0], orient[1], orient[2] = orient[2], orient[0], orient[1]
    elif _ == "R":
        perm[1], perm[3], perm[4] = perm[3], perm[4], perm[1]
        centers[1] = (centers[1] + 1) % 3
        orient[1], orient[3], orient[4] = orient[3], (orient[4] + 1) % 2, (orient[1] + 1) % 2
    elif _ == "R'":
        perm[1], perm[3], perm[4] = perm[4], perm[1], perm[3]
        centers[1] = (centers[1] - 1) % 3
        orient[1], orient[3], orient[4] = (orient[4] + 1) % 2, orient[1], (orient[3] + 1) % 2
    elif _ == "L":
        perm[0], perm[5], perm[3] = perm[5], perm[3], perm[0]
        centers[2] = (centers[2] + 1) % 3
        orient[0], orient[5], orient[3] = orient[5], (orient[3] + 1) % 2, (orient[1] + 1) % 2
    elif _ == "L'":
        perm[0], perm[5], perm[3] = perm[3], perm[0], perm[5]
        centers[2] = (centers[2] - 1) % 3
        orient[0], orient[5], orient[3] = (orient[3] + 1) % 2, orient[1], (orient[5] + 1) % 2
    elif _ == "B":
        perm[2], perm[4], perm[5] = perm[4], perm[5], perm[2]
        centers[3] = (centers[3] + 1) % 3
        orient[2], orient[4], orient[5] = orient[4], (orient[5] + 1) % 2, (orient[2] + 1) % 2
    elif _ == "B'":
        perm[2], perm[4], perm[5] = perm[5], perm[2], perm[4]
        centers[3] = (centers[3] - 1) % 3
        orient[2], orient[4], orient[5] = (orient[5] + 1) % 2, orient[2], (orient[4] + 1) % 2

def move(currentMove):
    global permCopy
    global centersCopy
    global orientCopy
    if currentMove == 'U':
        permCopy[0], permCopy[1], permCopy[2] = permCopy[1], permCopy[2], permCopy[0]
        centersCopy[0] = (centersCopy[0] + 1) % 3
        orientCopy[0], orientCopy[1], orientCopy[2] = orientCopy[1], orientCopy[2], orientCopy[0]
    elif currentMove == "U'":
        permCopy[0], permCopy[1], permCopy[2] = permCopy[2], permCopy[0], permCopy[1]
        centersCopy[0] = (centersCopy[0] - 1) % 3
        orientCopy[0], orientCopy[1], orientCopy[2] = orientCopy[2], orientCopy[0], orientCopy[1]
    elif currentMove == "R":
        permCopy[1], permCopy[3], permCopy[4] = permCopy[3], permCopy[4], permCopy[1]
        centersCopy[1] = (centersCopy[1] + 1) % 3
        orientCopy[1], orientCopy[3], orientCopy[4] = orientCopy[3], (orientCopy[4] + 1) % 2, (orientCopy[1] + 1) % 2
    elif currentMove == "R'":
        permCopy[1], permCopy[3], permCopy[4] = permCopy[4], permCopy[1], permCopy[3]
        centersCopy[1] = (centersCopy[1] - 1) % 3
        orientCopy[1], orientCopy[3], orientCopy[4] = (orientCopy[4] + 1) % 2, orientCopy[1], (orientCopy[3] + 1) % 2
    elif currentMove == "L":
        permCopy[0], permCopy[5], permCopy[3] = permCopy[5], permCopy[3], permCopy[0]
        centersCopy[2] = (centersCopy[2] + 1) % 3
        orientCopy[0], orientCopy[5], orientCopy[3] = orientCopy[5], (orientCopy[3] + 1) % 2, (orientCopy[1] + 1) % 2
    elif currentMove == "L'":
        permCopy[0], permCopy[5], permCopy[3] = permCopy[3], permCopy[0], permCopy[5]
        centersCopy[2] = (centersCopy[2] - 1) % 3
        orientCopy[0], orientCopy[5], orientCopy[3] = (orientCopy[3] + 1) % 2, orientCopy[1], (orientCopy[5] + 1) % 2
    elif currentMove == "B":
        permCopy[2], permCopy[4], permCopy[5] = permCopy[4], permCopy[5], permCopy[2]
        centersCopy[3] = (centersCopy[3] + 1) % 3
        orientCopy[2], orientCopy[4], orientCopy[5] = orientCopy[4], (orientCopy[5] + 1) % 2, (orientCopy[2] + 1) % 2
    elif currentMove == "B'":
        permCopy[2], permCopy[4], permCopy[5] = permCopy[5], permCopy[2], permCopy[4]
        centersCopy[3] = (centersCopy[3] - 1) % 3
        orientCopy[2], orientCopy[4], orientCopy[5] = (orientCopy[5] + 1) % 2, orientCopy[2], (orientCopy[4] + 1) % 2


solutions = ["U", "U'", "R", "R'", "L", "L'", "B", "B'"]

def sols(n): #find all move sequences of length n
    global solutions
    if n == 1:
        pass
    else:
        for j in range(len(solutions)):
            if (solutions[j][-1] == "U" or (solutions[j].split())[-1] == "U'"):
                solutions[j] = [solutions[j] + " R", solutions[j] + " R'", solutions[j] + " L", solutions[j] + " L'", solutions[j] + " B", solutions[j] + " B'"]
            elif (solutions[j][-1] == "R" or (solutions[j].split())[-1] == "R'"):
                solutions[j] = [solutions[j] + " U", solutions[j] + " U'", solutions[j] + " L", solutions[j] + " L'", solutions[j] + " B", solutions[j] + " B'"]
            elif (solutions[j][-1] == "L" or (solutions[j].split())[-1] == "L'"):
                solutions[j] = [solutions[j] + " R", solutions[j] + " R'", solutions[j] + " U", solutions[j] + " U'", solutions[j] + " B", solutions[j] + " B'"]
            elif (solutions[j][-1] == "B" or (solutions[j].split())[-1] == "B'"):
                solutions[j] = [solutions[j] + " R", solutions[j] + " R'", solutions[j] + " L", solutions[j] + " L'", solutions[j] + " U", solutions[j] + " U'"]
        solutions = np.array(solutions).flatten()
        solutions = solutions.tolist()

for a in range(1, 6): #solution length can be 1-5.  THIS IS HOW YOU MODIFY POSSIBLE SOLUTION LENGTHS
    #test a solution of length a
    #print solution out if it works
    #repeat for all possible solutions of length a
    sols(a)
    for b in solutions:
        b = b.split()
        permCopy = copy.deepcopy(perm)
        orientCopy = copy.deepcopy(orient)
        centersCopy = copy.deepcopy(centers)
        #print(len(b))
        for c in range(len(b)):
            #print(b[c])
            move(b[c])
        if ((centersCopy[0] == 0 and centersCopy[1] == 0 and centersCopy[2] == 0 and ((permCopy[0] == 0 and permCopy[1] == 1 and orientCopy[0] == 0 and orientCopy[1] == 0) or (permCopy[0] == 0 and permCopy[3] == 3 and orientCopy[0] == 0 and orientCopy[3] == 0) or (permCopy[1] == 1 and permCopy[3] == 3 and orientCopy[1] == 0 and orientCopy[3] == 0))) or (centersCopy[0] == 0 and centersCopy[1] == 0 and centersCopy[3] == 0 and ((permCopy[1] == 1 and permCopy[2] == 2 and orientCopy[1] == 0 and orientCopy[2] == 0) or (permCopy[1] == 1 and permCopy[4] == 4 and orientCopy[1] == 0 and orientCopy[4] == 0) or (permCopy[2] == 2 and permCopy[4] == 4 and orientCopy[2] == 0 and orientCopy[4] == 0))) or (centersCopy[0] == 0 and centersCopy[2] == 0 and centersCopy[3] == 0 and ((permCopy[0] == 0 and permCopy[2] == 2 and orientCopy[0] == 0 and orientCopy[2] == 0) or (permCopy[0] == 0 and permCopy[5] == 5 and orientCopy[0] == 0 and orientCopy[5] == 0) or (permCopy[2] == 2 and permCopy[5] == 5 and orientCopy[2] == 0 and orientCopy[5] == 0))) or (centersCopy[1] == 0 and centersCopy[2] == 0 and centersCopy[3] == 0 and ((permCopy[3] == 3 and permCopy[4] == 4 and orientCopy[3] == 0 and orientCopy[4] == 0) or (permCopy[3] == 3 and permCopy[5] == 5 and orientCopy[3] == 0 and orientCopy[5] == 0) or (permCopy[4] == 4 and permCopy[5] == 5 and orientCopy[4] == 0 and orientCopy[5] == 0)))):
            solutionAsString = ""
            for _ in b:
                solutionAsString += _
                solutionAsString += " "
            print(solutionAsString)