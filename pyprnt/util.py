import os

def get_terminal_size():
    try:
        return os.get_terminal_size().columns
    except:
        return 50

def border(position, width, label, value):
    if 3 + label + value > width:
        value = width - label - 3

    if position == "top":
        return "┌" + "─" * (label) + "┬" + "─" * (value) + "┐"
    elif position == "bottom":
        return "└" + "─" * (label) + "┴" + "─" * (value) + "┘"

def prnt_iteratable(obj, end, truncate, depth, width, file, flush):
    output = create_output(obj, truncate=truncate, level=0, depth=depth, width=width)
    print_output(output, end=end, file=file, flush=flush)
    
    if type(output) != list:
        return output
    else:
        return "\n".join(output)

def create_output(obj, truncate, level, depth, width):
    # This function is RECURSIVE
    if width < 10:
        return str(obj)
    if level == depth:
        return str(obj)
    if len(obj) == 0:
        return str(obj)

    if type(obj) == list:
        label = str(len(obj)-1)
        max_label_length = len(label)
        value = list(map(str, obj))
        max_value_length = len(max(value, key=len))
        iterate_items = enumerate(obj)
    elif type(obj) == dict:
        label = list([str(key) for key in obj.keys()])
        max_label_length = len(max(label, key=len))
        value = list(map(str, obj.values()))
        max_value_length = len(max(value, key=len))
        iterate_items = obj.items()
    else:
        raise TypeError('need a list or a dictionary')

    # Resize if the label is too long
    half_width = int(width/2)-1
    if max_label_length > half_width:
        max_label_length = half_width
        allowed_space = allowed_space = width - max_label_length - 3

    # Prepare output
    output = []
    allowed_space = width - max_label_length - 3 # Max Allowed Space for Value
    top_border = border("top", width, max_label_length, max_value_length)
    bottom_border = border("bottom", width, max_label_length, max_value_length)
    
    output.append(top_border)
    for i, j in iterate_items:
        # Label
        label = str(i)
        label_empty = " " * (max_label_length - len(label))
        # Truncate if the label is too long
        if len(label) > half_width:
            label = label[:half_width-3] + "..."
            label_empty = ""

        # Value
        if type(j) == list or type(j) == dict:
            value = create_output(j, truncate=truncate, level=level+1, depth=depth, width=width-max_label_length-3)
        else:
            value = str(j)
        if allowed_space > max_value_length:
            value_empty = " " * (max_value_length - len(value))
        else:
            value_empty = " " * (allowed_space - len(value))

        if type(value) != list and len(value) > allowed_space and not truncate:
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
            if type(value) == list:
                for ii, line in enumerate(value):
                    if ii > 0: label = " " * len(label)
                    # output.append(f"│{label}{label_empty}│{line}│") above 3.7
                    output.append("│{}{}│{}│".format(label, label_empty, line))
            else:
                if type(value) == str and len(value) > allowed_space:
                    value = value[:allowed_space - 3] + "..."
                output.append("│{}{}│{}{}│".format(label, label_empty, value, value_empty))
    output.append(bottom_border)
    output = tailor_output(output)
    return output

def tailor_output(output):
    if type(output) != list:
        return output

    top_border = output[0]
    bottom_border = output[len(output)-1]
    max_width = 0

    # Skip very first and very last
    for i in range(1, len(output)-1):
        row = output[i]
        if len(row) >= max_width:
            max_width = len(row)

    diff = max_width - len(top_border)

    if diff >= 0:
        top_border = top_border[:-1]
        top_border += "─" * (diff)
        top_border += "┐"
        bottom_border = bottom_border[:-1]
        bottom_border += "─" * (diff)
        bottom_border += "┘"
        output[0] = top_border
        output[len(output)-1] = bottom_border
    else:
        top_border = top_border[:diff-1]
        top_border += "─" * (diff)
        top_border += "┐"
        bottom_border = bottom_border[:diff-1]
        bottom_border += "─" * (diff)
        bottom_border += "┘"
        output[0] = top_border
        output[len(output)-1] = bottom_border

    for i in range(1, len(output)-1):
        row = output[i]
        diff = max_width - len(row)
        if diff > 0:
            output[i] = row[:-1] + (" " * (diff)) + "│"
    
    return output

def print_output(output, end, file, flush):
    if type(output) == str:
        print(output, end='', file=file, flush=flush)
        return
    for i, line in enumerate(output):
        if i < len(output) - 1: print(line, file=file, flush=flush)
        else: print(line, end='', file=file, flush=flush)
