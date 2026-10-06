import abc

"""
This module defines marginalizations to draw
samples of non-marginalized parameters and compute appropriate probability
"""

class Marginalizer(abc.ABC):

    QUANT_TYPES = []
    JITTER_PARAMS = []
    REQ_PARAMS = []
    MARG_PARAMS = []
    LNLIKE_TYPE = None
    MULTIBODY = False
    
    @abc.abstractmethod
    def apply(self, param_arr, jitter_arr=None, calculated_values={}):
        pass

class Marg1(Marginalizer):

    REQ_PARAMS = ["tau", "per"]
    MARG_PARAMS = ["sma", "pan"]

class Marg2(Marginalizer):

    REQ_PARAMS = ["tau", "sma", "pan"]
    MARG_PARAMS = ["gamma"]

def compatible_params(marginalizers, input_params):
    # TODO: Multibody, quant_type
    params = set(input_params)
    for marginalizer in marginalizers:
        req_params = set(marginalizer.REQ_PARAMS)
        marg_params = set(marginalizer.MARG_PARAMS)
        if len(req_params - params) == 0 and len(marg_params & params) == 0:
            params |= set(marginalizer.MARG_PARAMS)
        else:
            return False
    return True