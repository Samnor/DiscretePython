

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
