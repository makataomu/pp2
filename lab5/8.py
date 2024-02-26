import re
from functions import split_at_uppercase, replace

replace(pattern=r"(?=[A-Z][^A-Z])", replave_value=" ")