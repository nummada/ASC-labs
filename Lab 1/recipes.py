
"""Reads the recipes from files"""
def read_recipe(type_of_coffee):
    input_file = open("recipes/" + type_of_coffee + ".txt", "r")
    input_file.readline()
    values = input_file.readlines()
    water = int(values[0][6:])
    coffee = int(values[1][7:])
    milk = int(values[2][5:])

    return {"water": water, "coffee": coffee, "milk": milk}
