import sys
import unittest
from os import path
from models.dojo import Dojo
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

    def test_office_created_successfully(self):
        initial_room_count = len(self.dojo.offices)
        self.office2 = self.dojo.create_room('Hogwarts', 'office')
        new_room_count = len(self.dojo.offices)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_living_rooms_created_successfully(self):
        initial_room_count = len(self.rooms)
        self.living = self.dojo.create_room('Python', 'livingspace')
        new_room_count = len(self.rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_office_creation_duplicate(self):
        initial_room_count = len(self.rooms)
        self.office1 = self.dojo.create_room('Valhalla', 'office')
        new_room_count = len(self.offices)
        self.assertEqual(new_room_count - initial_room_count, 0)

    def test_livingspace_creation_duplicate(self):
        initial_room_count = len(self.rooms)
        self.room2 = self.dojo.create_room('Nexus', 'livingspace')
        new_room_count = len(self.rooms)
        self.assertEqual(new_room_count - initial_room_count, 0)


class AddPersonTestCases(unittest.TestCase):
    """Tests all the functionality of create_room method.
    """
    def setUp(self):
        """Create an instance of  the class dojo and pass it all tests in test case
        """
        self.dojo = Dojo()
        self.fellow1 = self.dojo.add_person('Salat', 'Abdala', 'Fellow')
        self.staff1 = self.dojo.add_person('Naima', 'Hussein', 'Staff')
        self.office1 = self.dojo.create_room('Argon', 'office')
        self.room1 = self.dojo.create_room('west', 'livingspace')
        self.fellow_name = self.dojo.fellows[0].fname
        self.staff_name = self.dojo.staff[0].fname
        self.room_capacity = self.dojo.all_rooms[0].room_capacity

    def test_fellow_added_successfully(self):
        initial_fellow_count = len(self.dojo.fellows)
        self.fellow2 = self.dojo.add_person('Burei', 'Dollar', 'Fellow')
        new_fellow_count = len(self.dojo.fellows)
        self.assertEqual(new_fellow_count - initial_fellow_count, 1)

    def test_fellow_wants_room_added_successfully(self):
        initial_fellow_count = len(self.dojo.fellows)
        self.fellow3 = self.dojo.add_person('Jackie', 'Macharia', 'Fellow', 'Y')
        new_fellow_count = len(self.dojo.fellows)
        self.assertEqual(new_fellow_count - initial_fellow_count, 1)

    def test_staff_added_successfully(self):
        initial_staff_count = len(self.dojo.staff)
        self.staff2 = self.dojo.add_person('Eva', 'Njeri', 'Staff')
        new_staff_count = len(self.dojo.staff)
        self.assertEqual(new_staff_count - initial_staff_count, 1)

    def test_staff_duplicate(self):
        initial_staff_count = len(self.dojo.staff)
        self.staff2 = self.dojo.add_person('Naima', 'Hussein', 'Staff')
        new_staff_count = len(self.dojo.staff)
        self.assertEqual(new_staff_count - initial_staff_count, 0)

    def test_add_fellow_duplicate(self):
        self.fellow = self.dojo.add_person('Albert', 'Yusuf', 'Fellow', 'Y')
        print(self.dojo.fellows)
        initial_fellow_count = len(self.dojo.fellows)
        self.new_fellow = self.dojo.add_person('Albert', 'Yusuf', 'Fellow', 'Y')
        print(self.dojo.fellows)
        new_fellow_count = len(self.dojo.fellows)
        self.assertEqual(new_fellow_count - initial_fellow_count, 0)

    def test_fellow_room_allocation_successful(self):
        # if a fellow gets allocated the the room capacity should decrease by 1
        initial_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.fellow2 = self.dojo.add_person('Burei', 'Dollar', 'Fellow')
        new_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.assertEqual((new_room_capacity - initial_room_capacity), 1)

    def test_staff_room_allocation_successful(self):
        # if a staff member gets a room , room capacity should decrease by 1
        initial_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.staff2 = self.dojo.add_person('Naomi', 'Dollar', 'Staff')
        new_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.assertEqual((new_room_capacity - initial_room_capacity), 1)

    def test_unallocated_persons(self):
        initial_unallocated = len(self.dojo.unallocated)
        self.staff = self.dojo.add_person('Naomi', 'Dollar', 'Staff')
        new_unallocated = len(self.dojo.unallocated)
        self.assertEqual((new_unallocated - initial_unallocated), 0)

if __name__ == "__main__":
    unittest.main()
