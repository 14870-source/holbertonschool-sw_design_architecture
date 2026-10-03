#!/usr/bin/env python3


class Beverage:
    def cost(self):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError


class Coffee(Beverage):
    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class MilkDecorator(Beverage):
    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


def main():
    milk = MilkDecorator(Coffee())
    print(milk.description(), milk.cost())

    sugar_milk = MilkDecorator(SugarDecorator(Coffee()))
    print(sugar_milk.description(), sugar_milk.cost())

    caramel_milk_sugar = CaramelDecorator(
        MilkDecorator(SugarDecorator(Coffee()))
    )
    print(
        caramel_milk_sugar.description(),
        caramel_milk_sugar.cost()
    )


if __name__ == "__main__":
    main()
