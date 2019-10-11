# PyPrnt

[![Build Status](https://travis-ci.com/kevink1103/pyprnt.svg?branch=master)](https://travis-ci.com/kevink1103/pyprnt)
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
print(creation)
prnt(creation) # Magic!
print(menu)
prnt(menu) # Magic!
```

You should see this...

```text
['Adam', 'Eve']
┌─┬────┐
│0│Adam│
│1│Eve │
└─┴────┘
{'Kimchi': 5000, 'Ice Cream': 100}
┌─────────┬────┐
│Kimchi   │5000│
│Ice Cream│100 │
└─────────┴────┘
```

Wanna see more?  
Check out the content of a block with ease.

```python
block = {'index':1,'transaction':[{"sender":"Block_Reward","receipient":"30819f300d06092a864886f70d010101050003818d0030818902818100b9cadf2ca51ca6714cf645f015652a80b9b8fc7e1aafc888334ac6f4f7dc177465595ef713765b027ab97ca7929820d1afb54b64a03cb971f0f46582d5266568f78746d30c4a651b0a0cf14dacdd619f034b330f4c14f253c72496778ff921a1b907aa0e6201369bffb2bd2e0a059d034e711ef004a3100a8998c2786349579f0203010001","value":"5.0"},{"sender":"30819f300d06092a864886f70d010101050003818d0030818902818100b9cadf2ca51ca6714cf645f015652a80b9b8fc7e1aafc888334ac6f4f7dc177465595ef713765b027ab97ca7929820d1afb54b64a03cb971f0f46582d5266568f78746d30c4a651b0a0cf14dacdd619f034b330f4c14f253c72496778ff921a1b907aa0e6201369bffb2bd2e0a059d034e711ef004a3100a8998c2786349579f0203010001","receipient":"30819f300d06092a864886f70d010101050003818d0030818902818100ab65b338fc66d9fc4870b7319f3c21aaf5a0082bce02caf9e3de6dc159c9df91477786028e7380be451d2fb94ed83070e85b588b4ed9d540461d3256bd2aafd3ae0fefa92f82799064414d0ed9e667bc18ad0f48505a2ae9b790a4363fcbef4b526453f91e9572835feabb25aebe2ff38c9abff32b6140c39cb71f8cf0491b850203010001","value":5.0,"signature":"a3da555fe4afe5fc957d466161dbae8b7fbb02c22780cae6fd5a4bbdc3ad7b8753361f74948db662086209c4272ebdadf5b7a14216c18be7f1c3b86ddb3aa43267792f3edc99cc7294fa89bc95f90cfb0ecd2df73b0dde8520499836f86b57af79d837b3c3dc806a37d067ca4a55caee7883bec035fed0b2df40c910cdde99a2"}],'timestamp':'09/23/2019,16:08:19','previous_hash':'This_Is_Genesis_Block','hash':'00e63fb0a8474d78df37e0ba99816d526ba110fc16098ecae65358890975a645','nonce':222}

# print(block) - don't use this!
prnt(block, truncate=True) # Magic!
```

```text
┌─────────────┬──────────────────────────────────┐
│index        │1                                 │
│transaction  │┌─┬──────────────────────────────┐│
│             ││0│┌──────────┬─────────────────┐││
│             ││ ││sender    │Block_Reward     │││
│             ││ ││receipient│30819f300d0609...│││
│             ││ ││value     │5.0              │││
│             ││ │└──────────┴─────────────────┘││
│             ││1│┌──────────┬─────────────────┐││
│             ││ ││sender    │30819f300d0609...│││
│             ││ ││receipient│30819f300d0609...│││
│             ││ ││value     │5.0              │││
│             ││ ││signature │a3da555fe4afe5...│││
│             ││ │└──────────┴─────────────────┘││
│             │└─┴──────────────────────────────┘│
│timestamp    │09/23/2019,16:08:19               │
│previous_hash│This_Is_Genesis_Block             │
│hash         │00e63fb0a8474d78df37e0ba99816d5...│
│nonce        │222                               │
└─────────────┴──────────────────────────────────┘
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

### truncate: bool (default: False)

Truncate output values if they exceed the maximum width of Terminal.  
The maximum width of Terminal is 50 in this example.

```python
# truncate = False
prnt(["abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", 12345678910])
# truncate = True
prnt(["abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", 12345678910], truncate=True)
```

```text
┌─┬──────────────────────────────────────────────┐
│0│abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst│
│ │uvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmn│
│ │opqrstuvwxyz                                  │
│1│12345678910                                   │
└─┴──────────────────────────────────────────────┘
┌─┬──────────────────────────────────────────────┐
│0│abcdefghijklmnopqrstuvwxyzabcdefghijklmnopq...│
│1│12345678910                                   │
└─┴──────────────────────────────────────────────┘
```

### width: int (default: current Terminal width or 50)

Set the maximum width of Terminal.

```python
prnt(["Kevin Kim is a developer."], width=10)
```

```text
┌─┬──────┐
│0│Kevin │
│ │Kim is│
│ │ a dev│
│ │eloper│
│ │.     │
└─┴──────┘
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

Copyright (c) 2019 Kevin Kim  
[Website](https://kevink1103.github.io/) 
[GitHub](https://github.com/kevink1103) 
[LinkedIn](https://www.linkedin.com/in/kimsungbum/)
