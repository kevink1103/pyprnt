def __top_border(first, second):
    return "┌" + "─" * (first) + "┬" + "─" * (second) + "┐"

def __bottom_border(first, second):
    return "└" + "─" * (first) + "┴" + "─" * (second) + "┘"

def prnt_iteratable(obj, end):
    if type(obj) == list:
        first_col = str(len(obj)-1)
        max_first_length = len(first_col)
        second_col = list(map(str, obj))
        max_second_length = len(max(second_col, key=len))
        iterate_items = enumerate(obj)
    elif type(obj) == dict:
        first_col = list(obj.keys())
        max_first_length = len(max(first_col, key=len))
        second_col = list(map(str, obj.values()))
        max_second_length = len(max(second_col, key=len))
        iterate_items = obj.items()
    else:
        raise TypeError('Need a list or a dictionary')

    top_border = __top_border(max_first_length, max_second_length)
    bottom_border = __bottom_border(max_first_length, max_second_length)

    output = []
    output.append(top_border)
    for first, second in iterate_items:
        first_empty = " " * (max_first_length - len(str(first)))
        second_empty = " " * (max_second_length - len(str(second)))
        output.append("│{}{}│{}{}│".format(first, first_empty, second, second_empty))
    output.append(bottom_border)

    for i, line in enumerate(output):
        if i < len(output) - 1: print(line)
        else: print(line, end=end)
