import sys
from .helper import get_terminal_size, prnt_iteratable

__all__ = ['prnt']

def prnt(*obj, enable=True, both=False, truncate=False,
        width=get_terminal_size(),
        sep=' ', end='\n', file=sys.stdout, flush=False):
    # Separator in action
    if len(obj) > 1 and (sep != '' and sep != ' '):
        print(*obj, sep=sep, end=end, file=file, flush=flush)
        return

    for i, o in enumerate(obj):
        if enable and (type(o) == list or type(o) == dict):
            if both: print(o, sep=sep, file=file, flush=flush)
            
            prnt_iteratable(o, end='', truncate=truncate, width=width, file=file, flush=flush)
        else:
            temp_end = ' ' if i < len(obj)-1 else ''
            print(o, sep=sep, end=temp_end, file=file, flush=flush)
            if i < len(obj)-1 and (type(obj[i+1]) == list or type(obj[i+1]) == dict):
                print()
    print(end=end)
