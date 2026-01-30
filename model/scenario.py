from quantitative import Quantitative
from occurance import Occurance
from event import Event

from datetime import date

class Scenario:
    """ 
    Scenarios have Quantitative objects that may evolve throughout the scenario.
    They also require transitions between scenarios. 
    
    For example; The scenario from 18YR to 35YR might involve a high interest savings account that transitions to a low interest savings account.
    The transitions governed by operations. 
    
    The scenario will not store its own end date, as it is determined by the beginning of the next scenario. """

    begin_date: date

    quantitatives: List[Quantitative]
    occurances: List[Occurance]

    begin_events = List[Event]
    end_events = List[Event]

    def __init__(self, begin_date: date) -> None:
        self.quantitatives = []
        self.occurances = []

        self.begin_date = begin_date

        self.begin_events = []
        self.end_events = []

    def add_quantitative(self, quantitative: Quantitative) -> None:
        self.quantitatives.append(quantitative)

    def add_occurance(self, occurance: Occurance) -> None:
        self.occurances.append(occurance)

    def get_quantitatives(self) -> List[Quantitative]:
        return self.quantitatives

    def get_occurances(self) -> List[Occurance]:
        return self.occurances

    def scenario_end(self) -> None: # TODO: implement transitions
        pass

    def scenario_begin(self) -> None: # TODO: implement transitions
        pass