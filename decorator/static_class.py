class Calculator:

    # shared class variables
    allocated = 0

    def __init__(self, name):
        self.name = name
        Calculator.allocated += 1

    # by using static method decorator you don't have to include "self
    # on function signature; can call fn on main by saying Calculator.add
    # instead of calling it from object instance
    @staticmethod
    def add(x, y):
        return x + y

def main():
    c1 = Calculator("calcy the calculator")
    c2 = Calculator("hp 41cv")
    c3 = Calculator("TI 30")

    total = c1.add(2, 3)
    total += Calculator.add(2, 3)

    print(c1.name, "says the answer is", total)
    print(c2.name, "says the answer is", total)
    print(c3.name, "says the answer is", total)

    print(c3.allocated, Calculator.allocated)


main()

