from functions import replace

pattern = r"(?<!^)_(\w)"
repl_value = lambda match: match.group(1).upper()

replace(pattern, repl_value)