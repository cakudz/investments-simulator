from occurance import Occurance
from datetime import date

class Event(Occurance):
    """ An event is an occurance that is distinct from recurrances
    """
    def __init__(self, name: str, date: date) -> None:
        super().__init__(name, date)