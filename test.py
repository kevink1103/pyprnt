import unittest
from unittest.mock import patch
import sys
import io

from pyprnt.position import Position
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
        testee = border(Position.top, label=5, value=5, width=20)
        expect = '┌─────┬─────┐'
        self.assertEqual(testee, expect)
    
    def test_bottom_border(self):
        testee = border(Position.bottom, label=5, value=5, width=20)
        expect = '└─────┴─────┘'
        self.assertEqual(testee, expect)
    
    def test_exceed_border(self):
        testee1 = border(Position.top, label=5, value=20, width=20)
        testee2 = len(testee1)
        expect1 = '┌─────┬────────────┐'
        expect2 = 20
        self.assertEqual(testee1, expect1)
        self.assertEqual(testee2, expect2)

class TestPrintMethods(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_basic(self, mock_stdout):
        creation = ["Adam", "Eve"]
        prnt(creation, width=50)
        testee = mock_stdout.getvalue()
        expect = '┌─┬────┐\n│0│Adam│\n│1│Eve │\n└─┴────┘\n'
        self.assertEqual(testee, expect)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dict_basic(self, mock_stdout):
        menu = {"kimchi": 5000, "Ice Cream": 100}
        prnt(menu, width=50)
        testee = mock_stdout.getvalue()
        expect = '┌─────────┬────┐\n│kimchi   │5000│\n│Ice Cream│100 │\n└─────────┴────┘\n'
        self.assertEqual(testee, expect)

if __name__ == '__main__':
    unittest.main()
