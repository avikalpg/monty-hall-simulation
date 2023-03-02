Monty Hall Problem
===

## Introduction

The *Monty Hall problem* is a brain teaser, in the form of a probability puzzle, loosely based on the American television game show _Let's Make a Deal_ and named after its original host, Monty Hall. 
It goes like this:

<quote>
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?
</quote>

The standard assumptions here are:

1. The host must always open a door that was not picked by the contestant.
2. The host must always open a door to reveal a goat and never the car.
3. The host must always offer the chance to switch between the originally chosen door and the remaining closed door.

You can find more details about the problem on [its Wikipedia page](https://en.wikipedia.org/wiki/Monty_Hall_problem).

## Setup

You need to have Python installed in your computer.
This simulation only uses in-built libraries, so you don't have to worry about setting up a virtual environment.

One of the following commands should give you a version number.
```bash
python3 --version

# or

python --version
```

## How to run

To run the simulation, just run the `sim.py` file directly:

```bash
python3 sim.py
```
This will run 100 iterations of the Monty Hall problem and give you the number of time you'd win if you `stay` with your original choice, and the number of times you'd win if you `switch` to the other door.


You can also give it the number of iterations you want of the simulation using the `-n` flag:

```bash
python3 sim.py -n 10000
```

or 

```bash
python3 sim.py --iterations 10000
```

## Outcome

When you run this simulation, you can clearly see that the `stay`:`switch` ratio is clearly proportional to 1:2. 
This estiblishes that it is always more beneficial to switch when the above mentioned assumptions hold true.
