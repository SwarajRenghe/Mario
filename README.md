# Super Mario Clone
# Environment - Linux Terminal - Python

## Introduction
The application is written in _near-Vanilla_ Python. The only dependency
is the `colorama` library, in order to provide some colors to an
otherwise monochrome ASCII text environment.

## Structure

The application demonstrates common Object Oriented Programming concepts,
like inheritance, encapsulation, polymorphism and abstraction.
- Each Player / Enemy is a derived class of a common `Person` class.
- Each Obstacle, Scenery Item and Tile is a derived class of a common
`Obstacle` class.

## Running the Program

- Install all requirements by running the following command in a
Linux Terminal :
  - `pip3 install -r requirements.txt`
- If the location of the Python installation is not the default
location, add the following line to the top of the program
with the location of your python installation
  - `#!/usr/bin/env python`
- Run the program using the following command
  - `./main.py` (if you have included the prev line)
  - `python3 main.py` (normal run)

## Controls

- Traditional Movement Control Keys (W, A, D)
- To quit, press `q`

## File Structure

.
 * [main.py](./main.py)
 * [character.py](./character.py)
 * [input.py](./input.py)
 * [obstacle.py](./obstacle.py)
 * [board.py](./board.py)
 * [config.py](./config.py)
 * [requirements.txt](./requirements.txt)
 * [README.md](./README.md)
