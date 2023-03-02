import random

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
    # run the simulation n number of times
    num_iterations = 100
    cummulative = { "stay": 0, "switch": 0 }
    for i in range(0,100):
        result = sim()
        for key in cummulative.keys():
            cummulative[key] += result[key]

    print(cummulative)

main()
