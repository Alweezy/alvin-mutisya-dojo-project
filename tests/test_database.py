import unittest
import sys
from os import path
from models.dojo import Dojo

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class TestSaveState(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.create_room('Hogwarts', 'Office')
        self.dojo.load_people('models/allocation.txt')

    def test_database_created_successfully(self):
        self.dojo.save_state('models/dojo_test_database')
        self.assertEqual(path.exists('models/dojo_test_database.db'), True)

    def test_people_table_persist_correct(self):
        self.dojo.all_people = self.dojo.fellows + self.dojo.staff
        people = len(self.dojo.all_people)
        self.assertEqual(7, people)

class TestLoadState(unittest.TestCase):
        def setUp(self):
            self.dojo = Dojo()

        def test_data_loaded_successfully(self):
            self.dojo.load_state('models/dojo_test_database')
            self.assertEqual(path.exists('models/dojo_test_database.db'), True)



