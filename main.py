import sys
from colors import Empty, Unit, get_colors

DEPTH = 4

if len(sys.argv) > 1:
    level = int(sys.argv[1])
    print(f" >>> Loading level {level}")
else:
    print("Level should be defined in arguement")
    sys.exit(1)


level_file = open(f"levels/{level}.cones")
cones_num, empty_cones_num = map(int, level_file.readline().split())

cones = [[Empty() for i in range(DEPTH)] for i in range(cones_num + empty_cones_num)]
colors = get_colors(cones_num)
i = 0
for coneline in level_file:
    cones[i] = [colors[k] for k in map(lambda x: int(x) - 1, coneline.split())]
    i += 1

def print_cones():
    global cones, cones_num, empty_cones_num
    for k in range(DEPTH - 1, -1, -1):
        print(" |" + "| |".join([str(cone[k]) for cone in cones]) + "| ")
    print(" " + " -  " * len(cones) + " ")
    print(" " + " ".join(str(i + 1).center(3) for i in range(len(cones))) + " ")

def check_cones():
    global cones
    for c in cones:
        #print([c[0] == c[i] for i in range(DEPTH)])
        if not all(c[0] == c[i] for i in range(DEPTH)):
            return False
    return True

def total_rate_counter(full=False):
    global cones

    def count(cone):
        #print("COUNTING")
        prev_c = Empty()
        rate = 0
        row = None
        for c in cone:
            #print(c)
            if isinstance(c, Empty):
                break
            if c != prev_c:
                if (not isinstance(prev_c, Empty)):
                    #print(f"addind {2 ** (row - 1)}")
                    rate += 2 ** (row - 1)
                    rate -= 2
                row = 0
            row += 1
            prev_c = c
        if row is not None:
            rate += 2 ** (row - 1)
            #print(f"addind {2 ** (row - 1)}")
        return rate


    rate = [count(c) for c in cones]        
    if not full:
        rate = sum(rate)
    return rate


def move():
    global cones
    try:
        movecmd = input("Make your move: ")
    except EOFError:
        return ""
    except KeyboardInterrupt:
        return ""
    a, b = map(lambda x: int(x) - 1, movecmd.split())
    if a == b:
        return "Error. Can't move to the same spot"

    ai = DEPTH - 1
    bi = DEPTH - 1

    if not (0 <= a < len(cones) and 0 <= b < len(cones)):
        return "Error. Comand beyond range"

    while isinstance(cones[a][ai], Empty) and ai >= 0:
        ai -= 1

    while isinstance(cones[b][bi], Empty) and bi >= 0:
        bi -= 1

    bi += 1
    #print(ai, bi)

    if (ai == -1):
        return "Error. Forbidden Move. First cone is empty"
    if (bi == DEPTH):
        return "Error. Second cone is full"
    if (bi != 0 and cones[a][ai] != cones[b][bi - 1]):
        return "Error. Forbidden Move. Units can't be mixed"

    main_color = cones[a][ai]
    while (ai >= 0 and bi < DEPTH and cones[a][ai] == main_color):
        cones[a][ai], cones[b][bi] = cones[b][bi], cones[a][ai]
        ai -= 1
        bi += 1        
    return "Ok"

def game():
    move_id = 0
    while not check_cones():
        print_cones()
        print(f"Current rate: {total_rate_counter()}")
        print(f"Detailed: {total_rate_counter(full=True)}")
        logs = move()
        if not logs:
            print("\nThe game is stopped")
            return
        if logs.startswith("Error"):
            print(logs)
            continue
        move_id += 1
        print(f" --- --- MOVE: {move_id} --- ---")

    print_cones()
    print(f"Current rate: {total_rate_counter()}")
    print(f"Detailed: {total_rate_counter(full=True)}")
    print(f"Level {level} is done!")

game()