import re

def open_and_process_csv(  filename
                         , encoding='utf-8'
                         , strip_quotes=True
                         , name_index=1
                         , process_line_func=None
                         ):
    with open(filename, 'r', encoding=encoding) as csvfile:
        next(csvfile)
        for line in csvfile:

            row = line.strip().split(',')
            name = row[name_index].strip('"') if strip_quotes else row[name_index]

            if process_line_func is not None:
                yield process_line_func(name)


def find_matches(pattern, filename=r"lab5\data.csv"):
    def process_line(name):
        if re.match(pattern, name):
            return f"Match found in: {name}"

    for result in open_and_process_csv(filename, process_line_func=process_line):
        if result:
            print(result)


def replace(pattern, replave_value, filename=r"lab5\data.csv"):
    def process_line(name):
        new_name = re.sub(pattern, replave_value, name)
        if new_name != name:
            return new_name

    for result in open_and_process_csv(filename, process_line_func=process_line):
        if result:
            print(result)


def split_at_uppercase(filename=r"lab5\data.csv"):
    def process_line(name): 
        return re.findall(r"(?=[A-Z][^A-Z])", name)
    
    for result in open_and_process_csv(filename, process_line_func=process_line):
        if result:
            print(result)

def camel_to_snake(filename=r"lab5\data.csv"):
    def process_line(camel_case_string): 
        pattern = r"(?<!^)(?=[A-Z])"
        snake_case_string = re.sub(pattern, "_", camel_case_string).lower()

        if snake_case_string != camel_case_string:
            return snake_case_string

    for result in open_and_process_csv(filename, process_line_func=process_line):
        if result:
            print(result)


