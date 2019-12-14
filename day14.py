from util import filehelper
import math

FUEL = "FUEL"
ORE = "ORE"


class Element:
    def __init__(self, name: str, amount: int):
        self.name = name
        self.amount = amount

    @classmethod
    def from_string(cls, line: str):
        amount_and_chemical = line.split(" ")
        amount = int(amount_and_chemical[0])
        name = amount_and_chemical[1]
        return Element(name, amount)

    def __repr__(self):
        return f"Chemical(name={self.name}, amount={self.amount})"


class Reaction:
    def __init__(self, line: str):
        in_out = line.split(" => ")
        self.inputs = [Element.from_string(item) for item in in_out[0].split(", ")]
        self.output = Element.from_string(in_out[1])

    def __repr__(self):
        return f"Reactions(inputs={self.inputs}, output={self.output})"


class FuelFactory:
    def __init__(self, reactions: [Reaction]):
        self.reactions = reactions
        self.stored_chemicals = {}

    def get_amount_for_element(self, key: str) -> int:
        if key not in self.stored_chemicals:
            self.stored_chemicals[key] = 0

        return self.stored_chemicals[key]

    def store_more_of_element(self, key: str, amount: int) -> None:
        if key not in self.stored_chemicals:
            old_amount = 0
        else:
            old_amount = self.stored_chemicals[key]
        self.stored_chemicals[key] = amount + old_amount

    def clear_element(self, key: str) -> None:
        self.stored_chemicals[key] = 0

    def get_reaction_for_element(self, key: str) -> Reaction:
        for reaction in self.reactions:
            if reaction.output.name == key:
                return reaction

    def perform_reaction(
        self, searched_element: Element,
    ):
        reaction = self.get_reaction_for_element(searched_element.name)
        times_applied = int(math.ceil(searched_element.amount / reaction.output.amount))
        total_cost = 0
        for chemical in reaction.inputs:
            new_amount = chemical.amount * times_applied
            costs = self.get_costs_for(Element(chemical.name, new_amount),)
            total_cost += costs

        self.store_more_of_element(
            searched_element.name,
            reaction.output.amount * times_applied - searched_element.amount,
        )
        return total_cost

    def get_costs_for(self, element: Element) -> int:
        if element.name == ORE:
            return element.amount
        if element.amount <= self.get_amount_for_element(element.name):
            self.store_more_of_element(element.name, -element.amount)
            return 0
        element.amount -= self.get_amount_for_element(element.name)
        self.clear_element(element.name)
        res = self.perform_reaction(element)

        return res

    def get_fuel_for(self, ore=1):
        costs = 0
        lower_bound = 0
        upper_bound = 1
        while costs < ore:
            costs = self.get_costs_for(Element(FUEL, upper_bound))
            if costs < ore:
                lower_bound = upper_bound
                upper_bound = upper_bound * 2

        while lower_bound + 1 < upper_bound:
            mid = (lower_bound + upper_bound) // 2
            costs = self.get_costs_for(Element(FUEL, mid))
            if costs > ore:
                upper_bound = mid
            elif costs < ore:
                lower_bound = mid
        return lower_bound


def day14_01():
    reaction_input = filehelper.get_string_list_from_file("./puzzles/14/puzzle.txt")
    reactions = [Reaction(line) for line in reaction_input]
    factory = FuelFactory(reactions)
    costs = factory.get_costs_for(Element(FUEL, 1))
    print(f"ore needed for one FUEL: {costs}")


def day14_02():
    reaction_input = filehelper.get_string_list_from_file("./puzzles/14/puzzle.txt")
    reactions = [Reaction(line) for line in reaction_input]
    factory = FuelFactory(reactions)
    target = 1000000000000
    fuel_needed = factory.get_fuel_for(target)
    print(f"fuel produced with {target} ore: {fuel_needed}")


if __name__ == "__main__":
    day14_01()
    day14_02()
