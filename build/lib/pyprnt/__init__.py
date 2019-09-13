import sys
from .helper import prnt_list, prnt_dict

def prnt(obj, enable=True, sep='', end='\n', file=sys.stdout, flush=False):
    if enable:
        if type(obj) == list:
            prnt_list(obj)
        elif type(obj) == dict:
            prnt_dict(obj)
        else:
            print(obj, sep=sep, end=end, file=file, flush=flush)
    else:
        print(obj, sep=sep, end=end, file=file, flush=flush)
