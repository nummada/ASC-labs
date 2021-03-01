"""
A command-line controlled coffee maker.
"""

import sys

"""
Implement the coffee maker's commands. Interact with the user via stdin and print to stdout.

Requirements:
    - use functions
    - use __main__ code block
    - access and modify dicts and/or lists
    - use at least once some string formatting (e.g. functions such as strip(), lower(),
    format()) and types of printing (e.g. "%s %s" % tuple(["a", "b"]) prints "a b"
    - BONUS: read the coffee recipes from a file, put the file-handling code in another module
    and import it (see the recipes/ folder)

There's a section in the lab with syntax and examples for each requirement.

Feel free to define more commands, other coffee types, more resources if you'd like and have time.
"""

"""
Tips:
*  Start by showing a message to the user to enter a command, remove our initial messages
*  Keep types of available coffees in a data structure such as a list or dict
e.g. a dict with coffee name as a key and another dict with resource mappings (resource:percent)
as value
"""

# Commands
EXIT = "exit"
LIST_COFFEES = "list"
MAKE_COFFEE = "make"  #!!! when making coffee you must first check that you have enough resources!
HELP = "help"
REFILL = "refill"
RESOURCE_STATUS = "status"
commands = [EXIT, LIST_COFFEES, MAKE_COFFEE, REFILL, RESOURCE_STATUS, HELP]

# Coffee examples
ESPRESSO = "espresso"
AMERICANO = "americano"
CAPPUCCINO = "cappuccino"

coffee_list = [ESPRESSO, AMERICANO, CAPPUCCINO]


# Resources examples
WATER = "water"
COFFEE = "coffee"
MILK = "milk"

# Coffee maker's resources - the values represent the fill percents
RESOURCES = {WATER: 100, COFFEE: 100, MILK: 100}

coffee_types = {AMERICANO: {WATER: 10, COFFEE: 10, MILK: 0},\
                CAPPUCCINO: {WATER: 5, COFFEE: 10, MILK: 10},\
                ESPRESSO: {WATER: 5, COFFEE: 10, MILK: 0}}

STATUS_FORMAT = "water: {WATER}% \ncoffee: {COFFEE}% \nmilk: {MILK}%"

"""
Example result/interactions:

I'm a smart coffee maker
Enter command:
list
americano, cappuccino, espresso
Enter command:
status
water: 100%
coffee: 100%
milk: 100%
Enter command:
make
Which coffee?
espresso
Here's your espresso!
Enter command:
refill
Which resource? Type 'all' for refilling everything
water
water: 100%
coffee: 90%
milk: 100%
Enter command:
exit
"""

def list_command():
    """ Displays coffee types """
    print(ESPRESSO + ", " + AMERICANO + ", " +  CAPPUCCINO)

def print_status():
    """ Displays info about the remaining resources """
    print(STATUS_FORMAT.format(WATER = RESOURCES[WATER],\
         COFFEE = RESOURCES[COFFEE], MILK = RESOURCES[MILK]))


def make_coffe_aux(type_of_coffee):
    """ Consumes the resources needed for coffee - Auxiliary function"""
    RESOURCES[WATER] -= coffee_types[type_of_coffee][WATER]
    RESOURCES[COFFEE] -= coffee_types[type_of_coffee][COFFEE]
    RESOURCES[MILK] -= coffee_types[type_of_coffee][MILK]


def make_coffee():
    """ Consumes the resources needed for coffee - Main function"""
    print("Which coffee?")
    type_of_coffee = sys.stdin.readline()[:-1]
    make_coffe_aux(type_of_coffee)
    print("Here's your espresso!")

def refill_aux(water, coffee, milk):
    """ Refills all the resources - Auxiliary function"""
    if water:
        RESOURCES[WATER] = 100
    if coffee:
        RESOURCES[COFFEE] = 100
    if milk:
        RESOURCES[MILK] = 100


def refill():
    """ Refills all the resources """
    print("Which resource? Type 'all' for refilling everything")
    who = sys.stdin.readline()[:-1]
    if who == "all":
        refill_aux(True, True, True)
    elif who == "water":
        refill_aux(True, False, False)
    elif who == "coffee":
        refill_aux(False, True, False)
    elif who == "milk":
        refill_aux(False, False, True)

def main():
    """ Main function """
    print("I'm a smart coffee maker")
    print("Enter command:")

    for line in sys.stdin:
        if line[:-1] == EXIT:
            break
        if line[:-1] == LIST_COFFEES:
            list_command()
        elif line[:-1] == RESOURCE_STATUS:
            print_status()
        elif line[:-1] == MAKE_COFFEE:
            make_coffee()
        elif line[:-1] == REFILL:
            refill()
        elif line[:-1] == HELP:
            print("\nAvailable commands are:")
            print(*commands, sep=", ")
            print("\nAvailable coffees are:")
            print(*coffee_list, sep=", ")

        print()


if __name__ == "__main__":
    main()
