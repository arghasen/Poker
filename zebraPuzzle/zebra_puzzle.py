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
        if imright(green, ivory)  # 6
        for (englishman, spaniard, ukranian, japanese, norwegian) in orderings
        if englishman is red  # 2
        if norwegian is first  # 10
        if nextto(norwegian, blue)  # 15
        for (coffee, tea, milk, ojdrink, water) in orderings
        if coffee is green  # 4
        if ukranian is tea  # 5
        if milk is middle  # 9
        if luckystrike is ojdrink  # 13
        for (oldgold, kools, chesterfields, luckystrike, parliaments) in orderings
        if kools is yellow  # 8
        if japanese is parliaments  # 14
        for (dog, snails, fox, horse, zebra) in orderings
        if spaniard is dog  # 3
        if oldgold is snails  # 7
        if nextto(chesterfields, fox)  # 11
        if nextto(kools, horse)  # 12
    )
