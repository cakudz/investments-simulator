from quantitative import Quantitative

class Operation:
    """ 
    An operation is a general formula of assignment,
    where names of quantitative objects are replaced with their values
    and the result is assigned to a quantitative object.
    
    For efficiency, the quantitative objects should be setup prior to instance creation so that
    the formula can be lazily evaluated. """

    expression: str
    target: str

    def __init__(self, formula: str):
        """ 
        Initialize the operation
        A formula for an operation is of the form LHS = RHS, 
        where LHS is a single object and RHS is a function. """

        args = formula.split("=")

        if len(args) != 2:
            raise ValueError("Operation formula must be of the form LHS = RHS")
        
        self.target = args[0].strip()
        self.expression = args[1].strip()

    def evaluate(self, quantitative_values: Dict[str, float]) -> float:
        """ Evaluate the expression using the given mapping of variables """
        return eval(self.expression, quantitative_values)

    def _evaluate(self, quantitative_values: List[Quantitative]) -> float:
        """ Evaluate expression by mapping variables """
        quantitative_references = {quantitative.get_name(): quantitative.get_value() for quantitative in quantitative_values}
        return self.evaluate(quantitative_references), quantitative_references

    def apply(self, quantitatives: List[Quantitative]):
        """ Evaluate the expression and assign the result to the target quantitative """
        result, quantitative_values = self._evaluate(quantitative_values)

        for quantitative in quantitatives:
            if quantitative.get_name() == self.target:
                quantitative.set_value(result)
                break
    
    def apply_transition(self, prev_quants: List[Quantitative], new_quants: List[Quantitative]):
        """ Use previous quantitative values and assign new quantitative values """
        result, quantitative_values = self._evaluate(prev_quants)

        for quantitative in new_quants:
            if quantitative.get_name() == self.target:
                quantitative.set_value(result)
                break
