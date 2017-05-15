import os
import sys
import unittest
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from dojo import Dojo


class TestsCasesRoom(unittest.TestCase):
    """Tests all the functionality of create_room method.
    """
    def setUp(self):
        """Creates an instance of the class dojo and passes instance to all tests
         in the test case.
        """
        self.dojo = Dojo()
        self.room_type = self.dojo.create_room.room_type
        self.room_name = self.dojo.create_room.room_name
        self.office1 = self.dojo.create_room('Valhalla', 'office')

    def test_room_created_successfully(self):
        initial_room_count = len(self.dojo.all_rooms)
        self.assertTrue(self.office1)
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_if_room_type_is_dict(self):
        self.assertEqual(self.room_type({}), 'room type can only be a string')

    def test_if_room_type_is_int(self):
        self.assertEqual(self.room_type(9), 'room type can only be a string')

    def test_if_room_type_is_list(self):
        self.assertEqual(self.room_type([]), 'room type can only be a string')

    def test_if_room_type_is_set(self):
        self.assertEqual(self.room_type(()), 'room type can only be a string')

    def test_if_room_type_is_valid(self):
        self.assertTrue(self.room_type, 'office' or 'livingspace')

    def test_room_name_is_not_int(self):
        self.assertEqual(self.room_name(9), 'room name can only be a string')

    def test_room_name_is_not_list(self):
        self.assertEqual(self.room_name([]), 'room name can only be a string')

    def test_room_name_is_not_dict(self):
        self.assertEqual(self.room_name({}), 'room name can only be a string')

    def test_room_name_is_not_set(self):
        self.assertEqual(self.room_name(()), 'room name can only be a string')


class PersonTestCases(unittest.TestCase):
    """Tests all the functionality of create_room method.
    """
    def setUp(self):
        """Create an instance of  the class dojo and pass it all tests in test case
        """
        self.dojo = Dojo()
        self.person = self.dojo.add_person()


if __name__ == "__main__":
    unittest.main()
