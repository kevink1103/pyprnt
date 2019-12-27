import sys
from pyprnt.util import get_terminal_size, prnt_iteratable

def prnt(*obj, enable=True, both=False, truncate=False,
        depth=-1, width=get_terminal_size(), output=False,
        sep=' ', end='\n', file=sys.stdout, flush=False):
    try:
        if width < 20:
            raise ValueError('width should be bigger than 20')
        if depth != -1 and depth <= 0:
            raise ValueError('depth should be either -1 or bigger than 0')

        # Separator in action
        if len(obj) > 1 and (sep != '' and sep != ' '):
            print(*obj, sep=sep, end=end, file=file, flush=flush)
            if output: return sep.join(obj)
            return

        output_data = ""

        for i, o in enumerate(obj):
            if enable and (type(o) == list or type(o) == dict):
                if both:
                    print(o, sep=sep, file=file, flush=flush)
                    output_data = str(o) + "\n"
                output_data += prnt_iteratable(o, end='', truncate=truncate, depth=depth, width=width, file=file, flush=flush)
            else:
                temp_end = ' ' if i < len(obj)-1 else ''
                print(o, sep=sep, end=temp_end, file=file, flush=flush)

                if output_data != None and len(output_data) > 0:
                    output_data += str(o) + temp_end
                else:
                    output_data = str(o) + temp_end

                if i < len(obj)-1 and (type(obj[i+1]) == list or type(obj[i+1]) == dict):
                    print()
        print(end=end)
        if end != '\n':
            output_data += end

        if output:
            return output_data
    except Exception as e:
        print(*obj)
        print(e)
