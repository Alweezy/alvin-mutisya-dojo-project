from people import Person, Fellow, Staff
from unittest import TestCase


class PersonTestCases(TestCase):
    """Tests the functionality of the person parent class
    """
    def setUp(self):
        """Passess an instance of class Person to all the methods in this class
        """
        self.person = Person('Oluwafemi', 'Sule', 'Fellow')

    def test_full_name_is_correct(self):
        self.assertEqual(self.person.get_person_name(), 'Oluwafemi Sule')


class FellowTestCases(TestCase):
    def setUp(self):
        self.fellow = Fellow('Nadia', 'Alexis')

    def test_if_inherits_from_Person(self):
        self.assertTrue(issubclass(Fellow, Person))

    def test_person_name_is_correct(self):
        self.assertEqual(self.fellow.get_person_name(), 'Nadia Alexis')


class StaffTestCases(TestCase):
    def setUp(self):
        self.staff = Staff('Nadia', 'Alexis')

    def test_if_inherits_from_Person(self):
        self.assertTrue(issubclass(Staff, Person))

    def test_full_name_is_correct(self):
        self.assertEqual(self.staff.get_person_name(), 'Nadia Alexis')
