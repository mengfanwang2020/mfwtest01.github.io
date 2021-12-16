import unittest
from chapter11_unitest_name_function import get_formatted_name

class NameFunctionTest(unittest.TestCase):

    def setUp(self):
        self.formatted_name = ['meng', 'fan', 'wang']

    def test_first_last_name(self):
        formatted_name = get_formatted_name(self.formatted_name[0], self.formatted_name[2])
        self.assertEqual(formatted_name, 'Meng Wang')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name(self.formatted_name[0], self.formatted_name[2], self.formatted_name[1])
        self.assertEqual(formatted_name, 'Meng Fan Wang')

unittest.main

'''
assertEqual(a, b)  核实 a == b
assertNotEqual(a, b)  a != b
assertTrue(x) assertFalse(x) 核实x是否为真
assertIn(item, list)  assertNoyIn(item, list) 核实item是否在list中
'''