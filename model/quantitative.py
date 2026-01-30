class Quantitative:
    """ A quantitative is a object with a name and a value """
    
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value

    def get_name(self) -> str:
        return self.name
    
    def get_value(self) -> float:
        return self.value

    def set_value(self, value: float):
        self.value = value