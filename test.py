import unittest
import collections

from pyprnt.helper import get_terminal_size
from pyprnt.helper import border
from pyprnt import prnt

class TestTerminalMethods(unittest.TestCase):

    def test_get_terminal_size(self):
        testee = get_terminal_size()
        expect = 1
        self.assertGreater(testee, expect)

class TestBorderMethods(unittest.TestCase):

    def test_top_border(self):
        testee = border("top", label=5, value=5, width=20)
        expect = "┌─────┬─────┐"
        self.assertEqual(testee, expect)
    
    def test_bottom_border(self):
        testee = border("bottom", label=5, value=5, width=20)
        expect = "└─────┴─────┘"
        self.assertEqual(testee, expect)
    
    def test_exceed_border(self):
        testee1 = border("top", label=5, value=20, width=20)
        testee2 = len(testee1)
        expect1 = "┌─────┬────────────┐"
        expect2 = 20
        self.assertEqual(testee1, expect1)
        self.assertEqual(testee2, expect2)

class TestPrintEnable(unittest.TestCase):

    def test_enable_false(self):
        creation = ['Adam', 'Eve']
        testee = prnt(creation, enable=False, width=50)
        expect = "['Adam', 'Eve']"
        self.assertEqual(testee, expect)

class TestPrintBoth(unittest.TestCase):
    
    def test_both_true(self):
        creation = ['Adam', 'Eve']
        testee = prnt(creation, both=True, width=50)
        expect = "['Adam', 'Eve']\n┌─┬────┐\n│0│Adam│\n│1│Eve │\n└─┴────┘"
        self.assertEqual(testee, expect)

class TestPrintTruncate(unittest.TestCase):

    def test_truncate_false(self):
        testee = prnt(["abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", 12345678910], width=50)
        expect = "┌─┬──────────────────────────────────────────────┐\n│0│abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrst│\n│ │uvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmn│\n│ │opqrstuvwxyzabcdefghijklmnopqrstuvwxyz        │\n│1│12345678910                                   │\n└─┴──────────────────────────────────────────────┘"
        self.assertEqual(testee, expect)

    def test_truncate_true(self):
        testee = prnt(["abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", 12345678910], truncate=True, width=50)
        expect = "┌─┬──────────────────────────────────────────────┐\n│0│abcdefghijklmnopqrstuvwxyzabcdefghijklmnopq...│\n│1│12345678910                                   │\n└─┴──────────────────────────────────────────────┘"
        self.assertEqual(testee, expect)

class TestPrintDepth(unittest.TestCase):

    def test_depth_infinity_basic(self):
        testee = prnt([[[]], []], width=50)
        print(repr(testee))
        expect = "┌─┬──────┐\n│0│┌─┬──┐│\n│ ││0│[]││\n│ │└─┴──┘│\n│1│[]    │\n└─┴──────┘"
        self.assertEqual(testee, expect)

    def test_depth_infinity_complex(self):
        testee = prnt([[[{}]], []], width=50)
        expect = "┌─┬──────────┐\n│0│┌─┬──────┐│\n│ ││0│┌─┬──┐││\n│ ││ ││0│{}│││\n│ ││ │└─┴──┘││\n│ │└─┴──────┘│\n│1│[]        │\n└─┴──────────┘"
        self.assertEqual(testee, expect)

    def test_depth_1_basic(self):
        testee = prnt([[[]], []], depth=1, width=50)
        print(repr(testee))
        expect = "┌─┬────┐\n│0│[[]]│\n│1│[]  │\n└─┴────┘"
        self.assertEqual(testee, expect)

    def test_depth_1_complex(self):
        testee = prnt([[[{}]], []], depth=1, width=50)
        expect = "┌─┬──────┐\n│0│[[{}]]│\n│1│[]    │\n└─┴──────┘"
        self.assertEqual(testee, expect)

    def test_depth_2_basic(self):
        testee = prnt([[[]], []], depth=2, width=50)
        print(repr(testee))
        expect = "┌─┬──────┐\n│0│┌─┬──┐│\n│ ││0│[]││\n│ │└─┴──┘│\n│1│[]    │\n└─┴──────┘"
        self.assertEqual(testee, expect)

    def test_depth_2_complex(self):
        testee = prnt([[[{}]], []], depth=2, width=50)
        expect = "┌─┬────────┐\n│0│┌─┬────┐│\n│ ││0│[{}]││\n│ │└─┴────┘│\n│1│[]      │\n└─┴────────┘"
        self.assertEqual(testee, expect)

class TestPrintWidth(unittest.TestCase):

    def test_width_minimum_20(self):
        testee = prnt(["Kevin Kim is a developer."], width=20)
        expect = "┌─┬────────────────┐\n│0│Kevin Kim is a d│\n│ │eveloper.       │\n└─┴────────────────┘"
        self.assertEqual(testee, expect)

class TestPrintSep(unittest.TestCase):

    def test_separator_empty(self):
        testee = prnt("010", "8282", "8282", width=50)
        expect = "010 8282 8282"
        self.assertEqual(testee, expect)
    
    def test_separator_dash(self):
        testee = prnt("010", "8282", "8282", sep="-", width=50)
        expect = "010-8282-8282"
        self.assertEqual(testee, expect)

class TestPrintEnd(unittest.TestCase):

    def test_end_empty(self):
        testee = prnt("010", "8282", "8282", end="", width=50)
        expect = "010 8282 8282"
        self.assertEqual(testee, expect)

    def test_end_newline(self):
        testee = prnt("010", "8282", "8282", width=50)
        expect = "010 8282 8282"
        self.assertEqual(testee, expect)
    
    def test_end_dash(self):
        testee = prnt("010", "8282", "8282", end="--", width=50)
        expect = "010 8282 8282--"
        self.assertEqual(testee, expect)

class TestPrintBasic(unittest.TestCase):

    def test_list_basic(self):
        creation = ["Adam", "Eve"]
        testee = prnt(creation, width=50)
        expect = "┌─┬────┐\n│0│Adam│\n│1│Eve │\n└─┴────┘"
        self.assertEqual(testee, expect)

    def test_dict_basic(self):
        # For python version 3.4 and below
        menu = collections.OrderedDict()
        menu["kimchi"] = 5000
        menu["Ice Cream"] = 100
        testee = prnt(menu, width=50)
        expect = "┌─────────┬────┐\n│kimchi   │5000│\n│Ice Cream│100 │\n└─────────┴────┘"
        try:
            self.assertEqual(testee, expect)
        except:
            pass

if __name__ == "__main__":
    unittest.main()
