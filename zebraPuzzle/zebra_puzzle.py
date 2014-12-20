"zebra puzzle Implemantaion in Python"
# Author: Argha Sen
# Start Date : 19th December 2014
import itertools
COLORS = ['R', 'Y', 'G', 'B', 'I']
NATIONALITY = ['E', 'S', 'N', 'J', 'U']
DRINKS = ['C', 'T', 'M', 'O', 'W']
PETS = ['D', 'S', 'F', 'H', 'Z']
SMOKES = ['O', 'K', 'C', 'L', 'P']


def imright(house1, house2):
    "Find if a house is right of the other"
    return house1-house2 == 1


def nextto(house1, house2):
    "Find if a house is next of the other"
    return abs(house1-house2) == 1


def zebra_puzzle():
    "Solve zebra puzzle"
    location = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(location))  # 1
    return next(
        (water, zebra)
        for (red, green, ivory, yellow, blue) in orderings
        for (englishman, spaniard, ukranian, japanese, norwegian) in orderings
        for (coffee, tea, milk, ojdrink, water) in orderings
        for (oldgold, kools, chesterfields, luckystrike, parliaments) in orderings
        for (dog, snails, fox, horse, zebra) in orderings
        if englishman is red  # 2
        if spaniard is dog  # 3
        if coffee is green  # 4
        if ukranian is tea  # 5
        if imright(green, ivory)  # 6
        if oldgold is snails  # 7
        if kools is yellow  # 8
        if milk is middle  # 9
        if norwegian is first  # 10
        if nextto(chesterfields, fox)  # 11
        if nextto(kools, horse)  # 12
        if luckystrike is ojdrink  # 13
        if japanese is parliaments  # 14
        if nextto(norwegian, blue)  # 15
    )
