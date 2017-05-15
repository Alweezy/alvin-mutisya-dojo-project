from rooms import Room, Office,  LivingSpace
from unittest import TestCase


class RoomTestCase(TestCase):

    def test_room_instance(self):
        self.valhalla = Room('Valhalla', 'office', 6)
        self.assertEqual(self.valhalla.room_name, 'Valhalla')


class OfficeSpaceTestCase(TestCase):

    def test_class_inherits_from_room(self):
        self.assertTrue(issubclass(Office, Room))

    def test_room_correct_room_capacity(self):
        self.valhalla = Office('Valhalla')
        self.assertEqual(self.valhalla.room_capacity, 6)


class LivingSpaceTestCase(TestCase):
    def test_class_inherits_from_room(self):
        self.assertTrue(issubclass(LivingSpace, Room))

    def test_room_correct_room_capacity(self):
        self.python = LivingSpace('Python')
        self.assertEqual(self.python.room_capacity, 4)