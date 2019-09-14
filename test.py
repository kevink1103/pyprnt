import unittest
import sys
import io

from pyprnt.position import Position
from pyprnt.helper import border
from pyprnt import prnt

class TestBorderMethods(unittest.TestCase):

    def test_top_border(self):
        testee = border(Position.top, 5, 5, 20)
        expect = '┌─────┬─────┐'
        self.assertEqual(testee, expect)
    
    def test_bottom_border(self):
        testee = border(Position.bottom, 5, 5, 20)
        expect = '└─────┴─────┘'
        self.assertEqual(testee, expect)
    
    def test_exceed_border(self):
        testee1 = border(Position.top, 5, 20, 20)
        testee2 = len(testee1)
        expect1 = '┌─────┬────────────┐'
        expect2 = 20
        self.assertEqual(testee1, expect1)
        self.assertEqual(testee2, expect2)

class TestPrintMethods(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_basic(self, mock_stdout):
        prnt(["Adam", "Eve"])
        testee = mock_stdout.getvalue()
        expect = '┌─┬────┐\n│0│Adam│\n│1│Eve │\n└─┴────┘\n'
        self.assertEqual(testee, expect)
    
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dict_basic(self, mock_stdout):
        prnt({"kimchi": 5000, "Ice Cream": 100})
        testee = mock_stdout.getvalue()
        expect = '┌─────────┬────┐\n│kimchi   │5000│\n│Ice Cream│100 │\n└─────────┴────┘\n'
        self.assertEqual(testee, expect)

if __name__ == '__main__':
    unittest.main()