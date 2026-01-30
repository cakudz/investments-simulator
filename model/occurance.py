from datetime import date

class Occurance:
    """ An occurance is a thing that effects a person at a time
    """

    def __init__(self, name: str, date: date) -> None:
        """ Initialize the occurance

        Args:
            name: The name of the occurance
            time: The number of years from the start of the scenario to the occurance
        """
        self.name = name
        self.date = date

    def get_name(self) -> str:
        return self.name
    
    def get_date(self) -> date:
        return self.date

    