import sys
from .helper import prnt_list, prnt_dict

def prnt(*obj, enable=True, both=False, truncate=True, sep='', end='\n', file=sys.stdout, flush=False):
    # Separator in action
    if len(obj) > 1 and sep != '':
        print(*obj, sep=sep, end=end, file=file, flush=flush)
        return

    for i, o in enumerate(obj):
        if enable and (type(o) == list or type(o) == dict):
            if both: print(o, sep=sep, end='\n', file=file, flush=flush)
            if type(o) == list: prnt_list(o, end=end)
            elif type(o) == dict: prnt_list(o, end=end)
        else:
            trailing = end if (len(obj) >= 1) and (i == len(obj) - 1) else " "
            print(o, sep=sep, end=trailing, file=file, flush=flush)
