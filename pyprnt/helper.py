def __top_border(first, second):
    return "┌" + "─" * (first) + "┬" + "─" * (second) + "┐"

def __bottom_border(first, second):
    return "└" + "─" * (first) + "┴" + "─" * (second) + "┘"

def prnt_list(obj, end):
    indexes = str(len(obj)-1)
    max_idx_length = len(indexes)
    values = list(map(str, obj))
    max_val_length = len(max(values, key=len))
    top_border = __top_border(max_idx_length, max_val_length)
    bottom_border = __bottom_border(max_idx_length, max_val_length)
    
    print(top_border)
    for idx, val in enumerate(obj):
        idx_empty = " " * (max_idx_length - len(str(idx)))
        val_empty = " " * (max_val_length - len(str(val)))
        text = "│{}{}│{}{}│".format(idx, idx_empty, val, val_empty)
        print(text)
    print(bottom_border, end=end)

def prnt_dict(obj, end):
    keys = list(obj.keys())
    max_key_length = len(max(keys, key=len))
    values = list(map(str, obj.values()))
    max_val_length = len(max(values, key=len))
    top_border = __top_border(max_key_length, max_val_length)
    bottom_border = __bottom_border(max_key_length, max_val_length)
    
    print(top_border)
    for key, val in obj.items():
        key_empty = " " * (max_key_length - len(str(key)))
        val_empty = " " * (max_val_length - len(str(val)))
        text = "│{}{}│{}{}│".format(key, key_empty, val, val_empty)
        print(text)
    print(bottom_border, end=end)
