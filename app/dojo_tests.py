import os
import sys
import unittest
from os import path
from dojo import Dojo
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class TestsCasesRoom(unittest.TestCase):
    """Tests all the functionality of create_room method.
    """
    def setUp(self):
        """Creates an instance of the class dojo and passes instance to all tests
         in the test case.
        """
        self.dojo = Dojo()
        self.office1 = self.dojo.create_room('Valhalla', 'office')
        self.room1 = self.dojo.create_room('Nexus', 'livingspace')
        self.office = self.dojo.offices[0].room_type
        self.office_name = self.dojo.offices[0].room_name
        self.offices = self.dojo.offices
        self.rooms = self.dojo.livingrooms
        self.all_rooms = self.dojo.all_rooms

    def test_room_created_successfully(self):
        initial_room_count = len(self.dojo.all_rooms)
        self.office2 = self.dojo.create_room('Valhalla', 'office')
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_office_created_successfully(self):
        initial_room_count = len(self.dojo.offices)
        self.office2 = self.dojo.create_room('Valhalla', 'office')
        new_room_count = len(self.dojo.offices)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_living_rooms_created_successfully(self):
        initial_room_count = len(self.rooms)
        self.living = self.dojo.create_room('Python', 'livingspace')
        new_room_count = len(self.rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_office_creation_repeated(self):
        initial_room_count = len(self.rooms)
        self.office1 = self.dojo.create_room('Valhalla', 'office')
        new_room_count = len(self.rooms)
        self.assertEqual(new_room_count - initial_room_count, 0)

    def test_livingspace_creation_repeated(self):
        initial_room_count = len(self.rooms)
        self.room1 = self.dojo.create_room('Nexus', 'livingspace')
        new_room_count = len(self.rooms)
        self.assertEqual(new_room_count - initial_room_count, 0)


class AddPersonTestCases(unittest.TestCase):
    """Tests all the functionality of create_room method.
    """
    def setUp(self):
        """Create an instance of  the class dojo and pass it all tests in test case
        """
        self.dojo = Dojo()
        self.person = self.dojo.add_person('Salat', 'Abdala', 'fellow')



if __name__ == "__main__":
    unittest.main()
