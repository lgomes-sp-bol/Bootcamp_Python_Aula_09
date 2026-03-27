from log_decorator import log_decorator
from time_measure_decorator import time_measure_decorator
from tenacity_decorator import get_user_input

@time_measure_decorator
@log_decorator
def soma(a, b):
    return a + b

soma(3, 5)  
soma(3, 8)  
soma(5, 9)  