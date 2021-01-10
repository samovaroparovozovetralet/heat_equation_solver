from main_func import *


class Yoo(MainFunc):
    # integration range
    start_range_list = [0, 0, 0]
    finish_range_list = [1, 1, 1]

    def find_self(self):
        self.expr = self.integrate_in_cube(self.green * self.right, self.var_list_,
                                      self.start_range_list, self.finish_range_list)
