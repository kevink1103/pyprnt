from collections.abc import Mapping

import sys

from pyprnt.util import get_terminal_size, prnt_iteratable, is_sequence_container

def prnt(*obj, enable=True, both=False, truncate=False,
        depth=-1, width=None, output=False,
        sep=' ', end='\n', file=sys.stdout, flush=False):
    width = width or get_terminal_size()

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
            if enable and (is_sequence_container(o) or isinstance(o, Mapping)):
                if both:
                    print(o, sep=sep, file=file, flush=flush)
                    output_data = str(o) + "\n"
                output_data += prnt_iteratable(o, end='', truncate=truncate, depth=depth, width=width, output=output, file=file, flush=flush, last=i==len(obj)-1)
            else:
                temp_end = ' ' if i < len(obj)-1 else ''
                print(o, sep=sep, end=temp_end, file=file, flush=flush)

                if output_data != None and len(output_data) > 0:
                    output_data += str(o) + temp_end
                else:
                    output_data = str(o) + temp_end

                if i < len(obj)-1 and (is_sequence_container(obj[i+1]) or isinstance(obj[i+1], Mapping)):
                    print()
        print(end=end)
        if end != '\n':
            output_data += end

        if output:
            return output_data
    except Exception as e:
        print(*obj)
        print(e)
