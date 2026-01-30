from person import Person

class Model:
    """ The model controls the logical flow of the simulation """

    def __init__(self) -> None:
        self.person = Person(18)

        first_scenario = self.person.get_scenario(0)

    # TODO: initialise a person with a sample scenario, try and run the scenario until age 100
