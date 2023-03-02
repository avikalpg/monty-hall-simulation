import random
import argparse

def sim():
    # setup: 3 options chosen at random
    prize = random.randint(0,2)

    choice = random.randint(0,2)

    # reveal the door without the prize
    revealable_doors = [x for x in range(0,3) if x != choice and x != prize]
    # print(revealable_doors, prize, choice)
    reveal = revealable_doors[0]
    switch = [x for x in range(0,3) if x != choice and x != reveal][0]
    return { "stay": prize == choice, "switch": prize == switch}

def main():
    # get the number of time the simulation should run (defaults to 100)
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--iterations", help="Number iterations of Monty Hall", type=int)
    args = parser.parse_args()
    num_iterations = args.iterations if args.iterations else 100

    # run the simulation n number of times
    cummulative = { "stay": 0, "switch": 0 }
    for i in range(0, num_iterations):
        result = sim()
        for key in cummulative.keys():
            cummulative[key] += result[key]

    print(cummulative)

main()
