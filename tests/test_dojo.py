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

    def test_print_room_with_no_occupants(self):
        self.dojo.create_room('Humus', 'livingspace')
        request = self.dojo.print_room('Humus')
        self.assertEqual(request, 'Room has currently no occupants!.')


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
        self.fellow_name = self.dojo.fellows[0].first_name
        self.staff_name = self.dojo.staff[0].first_name
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
        initial_unallocated = len(self.dojo.office_unallocated)
        self.staff = self.dojo.add_person('Naomi', 'Dollar', 'Staff')
        new_unallocated = len(self.dojo.office_unallocated)
        self.assertEqual((new_unallocated - initial_unallocated), 0)

    def test_staff_wants_accommodation(self):
        initial_room_capacity = len(self.dojo.all_rooms[0].occupants)
        print(self.dojo.all_rooms[1].room_type)
        self.dojo.add_person('Bill', 'Slay', 'Staff', 'Y')
        new_room_capacity = len(self.dojo.all_rooms[1].occupants)
        self.assertEqual((new_room_capacity - initial_room_capacity), 0)


class TestReallocationTestCases(unittest.TestCase):
    """Tests all the functionality in reallocating an Andelan from their current room;
    office or residential.
    """

    def setUp(self):
        self.dojo = Dojo()
        self.dojo.add_person('Nelly', 'Blue', 'Fellow')
        self.office1 = self.dojo.create_room('Valhalla', 'office')
        self.living1 = self.dojo.create_room('Python', 'livingspace')
        self.dojo.add_person('Alex', 'Brown', 'Staff')

    def test_reallocate_to_unavailable_room(self):
        initial_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.dojo.reallocate_person('stf1', 'Oculus')
        new_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.assertEqual((new_room_capacity - initial_room_capacity), 0)

    def test_reallocate_successful(self):
        self.dojo.all_rooms[0].room_type
        self.dojo.create_room('Hogwarts', 'office')
        initial_room_capacity = len(self.dojo.all_rooms[2].occupants)
        self.dojo.reallocate_person('stf53', 'Hogwarts')
        new_room_capacity = len(self.dojo.all_rooms[2].occupants)
        self.assertEqual((new_room_capacity - initial_room_capacity), 1)

    def test_reallocate_to_same_room(self):
        initial_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.reallocate = self.dojo.reallocate_person('stf28', 'Valhalla')
        new_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.assertEqual((new_room_capacity - initial_room_capacity), 0)

    def test_reallocate_unallocated_person(self):
        initial_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.reallocate = self.dojo.reallocate_person('fel27', 'Valhalla')
        new_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.assertEqual((new_room_capacity - initial_room_capacity), 0)

    def test_different_room_type_reallocation(self):
        initial_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.reallocate = self.dojo.reallocate_person('stf30', 'Python')
        new_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.assertEqual((new_room_capacity - initial_room_capacity), 0)

    def test_reallocate_non_existent_member(self):
        initial_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.reallocate = self.dojo.reallocate_person('stf21', 'Valhalla')
        new_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.assertEqual((new_room_capacity - initial_room_capacity), 0)


class TesTCasesLoadPeople(unittest.TestCase):
    def setUp(self):
        """Instantiates the class Dojo to perform tests for load people"""
        self.dojo = Dojo()

    def test_people_load_successful(self):
        self.dojo.create_room('Camelot', 'office')
        initial_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.dojo.load_people('./models/allocation.txt')
        new_room_capacity = len(self.dojo.all_rooms[0].occupants)
        print(new_room_capacity)
        self.assertEqual((new_room_capacity - initial_room_capacity), 6)

    def test_load_people_from_non_existent_file(self):
        self.dojo.create_room('Chambers', 'office')
        initial_room_capacity = len(self.dojo.all_rooms[0].occupants)
        self.dojo.load_people('./models/no_file.txt')
        new_room_capacity = len(self.dojo.all_rooms[0].occupants)
        print(new_room_capacity)
        self.assertEqual((new_room_capacity - initial_room_capacity), 0)


if __name__ == "__main__":
    unittest.main()
