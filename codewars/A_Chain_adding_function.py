class Add(int):
    def __call__(self, n):
        return Add(self + n)


assert Add(1)(2)(3) == 6
assert Add(2)(2)(2) == 6
assert Add(4)(6)(10) == 20