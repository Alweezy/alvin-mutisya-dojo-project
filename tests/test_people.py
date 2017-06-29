from unittest import TestCase
from models.people import Person, Fellow, Staff


class FellowTestCases(TestCase):
    def setUp(self):
        self.fellow = Fellow('Nadia', 'Alexis', 'Fellow')

    def test_if_inherits_from_Person(self):
        self.assertTrue(issubclass(Fellow, Person))

    def test_person_name_is_correct(self):
        self.assertEqual(self.fellow.first_name + ' ' + self.fellow.last_name, 'Nadia Alexis')

    def test_fellow_id_generation(self):
        self.assertEqual(self.fellow.id, 'fel57')


class StaffTestCases(TestCase):
    def setUp(self):
        self.staff = Staff('Nadia', 'Alexis', 'Staff')

    def test_if_inherits_from_Person(self):
        self.assertTrue(issubclass(Staff, Person))

    def test_full_name_is_correct(self):
        self.assertEqual(self.staff.first_name + ' ' + self.staff.last_name, 'Nadia Alexis')

    def test_staff_id_generation(self):
        self.assertEqual(self.staff.id, 'stf62')
