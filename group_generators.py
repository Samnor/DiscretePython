import itertools
from Group import Group


def test_z_addition_group():
    n = 8
    steps = 20
    start_element = 5

    z_n_group = Group(group_set=range(0, n),
                      bin_operation=lambda x, y: (x + y) % n)
    cycle_steps = z_n_group.get_element_cycle_steps(start_element, steps)
    for step in cycle_steps:
        if(step == start_element):
            print()
        print(f"{step}", end=f" ")


def test_z_multiplication_group():
    n = 9
    steps = 20
    start_element = 5

    z_n_group = Group(group_set=range(0, n),
                      bin_operation=lambda x, y: (x * y) % n)
    cycle_steps = z_n_group.get_element_cycle_steps(start_element, steps)
    for step in cycle_steps:
        if(step == start_element):
            print()
        print(f"{step}", end=f" ")


if __name__ == "__main__":
    test_z_multiplication_group()
