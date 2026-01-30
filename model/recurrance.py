from occurance import Occurance
from datetime import date

class Recurrance(Occurance):
    """ A recurrance is an occurance that is repeated 
    """

    def __init__(self, name: str, time: int, cadence): # TODO: figure out type of cadence
        """ Initialise the recurrance

        Args:
            name: The name of the occurance
            time: The number of years from the start of the scenario to the occurance
            cadence: The time period between recurrances
        """
        super().__init__(name, time)
        self.cadence = cadence
