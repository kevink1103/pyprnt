# PyPrnt

[![PyPI version](https://badge.fury.io/py/pyprnt.svg)](https://badge.fury.io/py/pyprnt)

PyPrnt helps you to print a list or a dictionary in an organized table form.  
Just try it out!  
Don't use `print()` anymore. Use `prnt()` for the rest of your life :)

## How to install

```bash
# If you have both Python 2 and 3,
pip3 install pyprnt
# If you only have Python 3,
pip install pyprnt
```

## How to use

```python
from pyprnt import prnt

creation = ["Adam", "Eve"]
menu = {
    "Kimchi": 5000,
    "Ice Cream": 100
}
prnt(creation)
prnt(menu)
```

You should see this...

```text
┌─┬────┐
│0│Adam│
│1│Eve │
└─┴────┘
┌─────────┬────┐
│Kimchi   │5000│
│Ice Cream│100 │
└─────────┴────┘
```

## And more...

### enable: bool (default: True)

Enable prnt() form.

```python
prnt(creation, enable=False)
```

```text
['Adam', 'Eve']
```

### both: bool (default: False)

Print in both original print() form and prnt() form.

```python
prnt(creation, both=True)
```

```text
['Adam', 'Eve']
┌─┬────┐
│0│Adam│
│1│Eve │
└─┴────┘
```

### sep: str  (default: '')

Put a separator between each input.

```python
prnt("010", "8282", "8282", sep="-")
```

```text
010-8282-8282
```

### end: str (default: '\n')

Put at the end of an output.

```python
prnt(creation, end="")
prnt("The force is with me")
```

```text
┌─┬────┐
│0│Adam│
│1│Eve │
└─┴────┘The force is with me
```

## Author

Kevin Kim  
[Website](https://kevink1103.github.io/) 
[GitHub](https://github.com/kevink1103) 
[LinkedIn](https://www.linkedin.com/in/kimsungbum/)
