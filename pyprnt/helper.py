import os

from .position import Position

def get_terminal_size():
    try:
        return os.get_terminal_size().columns
    except:
        return 50

def border(position, width, label, value):
    if 3 + label + value > width:
        value = width - label - 3

    if position == Position.top:
        return "┌" + "─" * (label) + "┬" + "─" * (value) + "┐"
    elif position == Position.bottom:
        return "└" + "─" * (label) + "┴" + "─" * (value) + "┘"

def prnt_iteratable(obj, end, truncate, width, file, flush):
    output = create_output(obj, truncate=truncate, width=width)
    print_output(output, end=end, file=file, flush=flush)

def create_output(obj, truncate, width):
    if type(obj) == list:
        label = str(len(obj)-1)
        max_label_length = len(label)
        value = list(map(str, obj))
        max_value_length = len(max(value, key=len))
        iterate_items = enumerate(obj)
    elif type(obj) == dict:
        label = list(obj.keys())
        max_label_length = len(max(label, key=len))
        value = list(map(str, obj.values()))
        max_value_length = len(max(value, key=len))
        iterate_items = obj.items()
    else:
        raise TypeError('Need a list or a dictionary')

    # Prepare output
    output = []
    allowed_space = width - max_label_length - 3
    top_border = border(Position.top, width, max_label_length, max_value_length)
    bottom_border = border(Position.bottom, width, max_label_length, max_value_length)
    
    output.append(top_border)
    for i, j in iterate_items:
        label = str(i)
        label_empty = " " * (max_label_length - len(label))
        value = str(j)

        if allowed_space > max_value_length:
            value_empty = " " * (max_value_length - len(value))
        else:
            value_empty = " " * (allowed_space - len(value))

        if len(value) > allowed_space and not truncate:
            # Extra rows to print full long value
            while (True):
                if len(value) == 0:
                    break

                new_value = value[:allowed_space]
                value_empty = " " * (allowed_space - len(new_value))
                output.append("│{}{}│{}{}│".format(label, label_empty, new_value, value_empty))
                label = " " * (max_label_length)
                label_empty = ""
                value = value[allowed_space:]
        else:
            if len(value) > allowed_space:
                value = value[:allowed_space - 3] + "..."
            output.append("│{}{}│{}{}│".format(label, label_empty, value, value_empty))
    output.append(bottom_border)
    return output

def print_output(output, end, file, flush):
    for i, line in enumerate(output):
        if i < len(output) - 1: print(line, file=file, flush=flush)
        else: print(line, end='', file=file, flush=flush)
