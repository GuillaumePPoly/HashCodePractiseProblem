import numpy as np
from sys import argv, stdin


def file_parser():
    max_slices, nb_pizza = input().split(" ")
    arr_pizza = input().split(" ")
    arr_pizza = [int(pizza_str) for pizza_str in arr_pizza]
    return int(max_slices), int(nb_pizza), arr_pizza


def select_pizzas(max_slices, nb_pizza, arr_pizza):

    index = nb_pizza-1
    total_slices = 0
    chosen_pizza = []
    nb_pizza = 0
    while total_slices < max_slices and index >= 0:
        if total_slices + arr_pizza[index] <= max_slices:
            nb_pizza += 1
            chosen_pizza.append(index)
            total_slices += arr_pizza[index]
        index -= 1
    return nb_pizza, chosen_pizza


def print_solution_to_stdout(nb_chosen_pizza, chosen_pizza):
    print("{}".format(nb_chosen_pizza))
    chosen_pizza = [str(pizza_int) for pizza_int in chosen_pizza]
    print(" ".join(chosen_pizza), end='')


def create_solution():
    max_slices, nb_pizza, arr_pizza = file_parser()
    nb_chosen_pizza, chosen_pizza = select_pizzas(max_slices, nb_pizza, arr_pizza)
    print_solution_to_stdout(nb_chosen_pizza, chosen_pizza)


if __name__=="__main__":
    create_solution()
