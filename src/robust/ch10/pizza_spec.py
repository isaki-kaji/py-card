class PizzaSpecification:
    def __init__(self, dough_radius_in_inches: int, toppings: list[str]):
        assert (
            6 <= dough_radius_in_inches <= 12
        )

        self.__dough_radius_in_inches = dough_radius_in_inches
        self.__toppings: list[str] = toppings
        for topping in toppings:
            self.add_topping(topping)

    def add_toopping(self, topping: str):
        if is_sauce(topping) and any(t for t in self.__toppings if is_sauce(t)):
            raise Exception("ソースは1種類です。")
        if is_sauce(topping):
            self.__toppings.insert(0, topping)
        else:
            self.__toppings.append(topping)


def is_sauce(topping: str) -> bool:
    return True
