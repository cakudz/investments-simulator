from scenario import Scenario
from datetime import date

class Person:
    """ An object that represents a person in the real world that 
    is affected by sequential scenarios. 
    The first scenario should contain all initial data for the person.
    The Person object itself should only contain information that is 
    indendent of the scenarios. (e.g age)
    """

    scenarios: list[Scenario]
    age: int

    def __init__(self, age: int) -> None:
        """ Initialize the person with an initial scenario

        Args:
            age: The age of the person, note that this will be the age of
             the person at the start of the first scenario
        """
        self.scenarios = []
        self.age = age

        self.scenarios.append(Scenario(date.today()))

    def add_scenario(self, scenario: Scenario) -> None:
        self.scenarios.append(scenario)

    def get_scenarios(self) -> List[Scenario]:
        return self.scenarios

    def get_scenario(self, index: int) -> Scenario:
        return self.scenarios[index]