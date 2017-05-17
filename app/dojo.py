from models.people.people import Staff, Fellow
from models.rooms.rooms import Office, LivingSpace
import random


class Dojo(object):
    def __init__(self):
        self.offices = []
        self.livingrooms = []
        self.staff = []
        self.fellows = []
        self.all_rooms = []
        self.all_people = []

    def get_room(self, rooms):
        """A function to generate a list of random rooms with space.
        :param rooms:
        :return: room_name
        """
        # a room is only available if it's capacity is not exceeded
        available_rooms = [room for room in rooms if len(room.occupants) < room.room_capacity]
        # return False if all rooms are full
        if len(available_rooms) < 1:
            return False
        # choose a room fro the list of available rooms.
        chosen_room = random.choice(available_rooms)
        return chosen_room.room_name

    def create_room(self, room_name, room_type):
            if room_type is 'office':
                if room_name not in [room.room_name for room in self.offices]:
                    room = Office(room_name=room_name, room_type=room_type)
                    self.offices.append(room)
                    self.all_rooms.append(room)
                    return 'An office called' + ' ' + room_name + ' ' + 'has been successfully created'
                return 'An office with that name already exists'
            if room_type is 'livingspace':
                if room_name not in [room.room_name for room in self.livingrooms]:
                    room = LivingSpace(room_name=room_name, room_type=room_type)
                    # add object to list( has both room_name and room_type)
                    self.livingrooms.append(room)
                    self.all_rooms.append(room)
                    return 'A room called ' + room_name + ' has been successfully created!'
                return 'A living room with that name already exists'

    