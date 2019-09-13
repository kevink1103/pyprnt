import sys
from .helper import prnt_list, prnt_dict

def prnt(*obj, enable=True, sep='', end='\n', file=sys.stdout, flush=False):
    if (len(obj) > 1 and sep != '') or (len(obj) <= 1 and sep == ''):
        print(*obj, sep=sep, end=end, file=file, flush=flush)
        return

    for i, o in enumerate(obj):
        if enable and type(o) == list:
            prnt_list(o, end='\n')
        elif enable and type(o) == dict:
            prnt_dict(o, end='\n')
        else:
            if (sep == '') and (i != len(obj) - 1):
                print(o, sep=sep, end=' ', file=file, flush=flush)
            else:
                print(o, sep=sep, end=end, file=file, flush=flush)
