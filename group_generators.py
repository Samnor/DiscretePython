

class Group:
    def __init__(self, group_set, bin_operation):
        self.set = group_set
        self.star = bin_operation

    def get_element_cycle_steps(self, start_element, steps):
        current_element = start_element
        yield current_element
        for i in range(steps):
            current_element = self.star(current_element, start_element)
            yield current_element


def test_z_n_group():
    n = 8
    steps = 20
    start_element = 5
    z_n_group = Group(group_set=range(0,n), bin_operation=lambda x,y: (x + y) % n)
    cycle_steps = z_n_group.get_element_cycle_steps(start_element, steps)
    for step in cycle_steps:
        print(f"{step if step != start_element else 'CYCLE START'}")

if __name__ == "__main__":
    test_z_n_group()

