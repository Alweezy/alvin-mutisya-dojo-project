import sys
from os import path
from abc import ABCMeta, abstractmethod
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class Room:
    __metaclass__ = ABCMeta
    """Models the kind of rooms available at Andela,
        It forms the base class Room from which OfficeSpace and LivingRoom inherit"""
    def __init__(self, room_name, room_type, room_capacity):
        """Initializes the base class Room
        :param room_name: A string representing the name of the room
        :param room_type: A string representing the type of room, whether office or residential
        :param room_capacity: An integer representing the amount of space per room.
        """
        self.room_name = room_name
        self.room_type = room_type
        self.room_capacity = room_capacity
        self.occupants = []

    @abstractmethod
    def __repr__(self):
        return self.room_name


class Office(Room):

    def __init__(self, room_name, room_type):
        super(Office, self).__init__(room_name, room_type, room_capacity=6)

    def __repr__(self):
        return self.room_name


class LivingSpace(Room):

    def __init__(self, room_name, room_type):
        super(LivingSpace, self).__init__(room_name, room_type, room_capacity=4)

    def __repr__(self):
        return self.room_name
