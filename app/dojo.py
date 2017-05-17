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

    def add_person(self, first_name, last_name, occupation, wants_accommodation=None):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self. wants_accommodation = wants_accommodation
        self.person_name = self.first_name + self.last_name
        if occupation is 'Fellow':
            if self.person_name not in [person.fname + person.lname for person in self.fellows]:
                person = Fellow(first_name, last_name, occupation, wants_accommodation)
                print(first_name + last_name + ' has been added successfully!')
                # check if fellow wants accommodation, it is set to 'N' by default
                accommodation = person.wants_accommodation
                if accommodation is None:
                    # if a fellow does not want  accommodation then they get only office space
                    self.fellows.append(person)
                    work_room = self.get_room(self.offices)
                    # if there is no available office space
                    if work_room:
                        for room in self.offices:
                            if room.room_name == work_room:
                                room.occupants.append(person)
                                # deduct room capacity to update
                                room.room_capacity -= 1
                                print('A ' + person.occupation + ' ' + person.fname + ' has been added to ' + work_room)
                            else:
                                print('All offices are occupied, add a new office')
                else:
                    # if a fellow does not want  accommodation then they get only office space
                    work_room = self.get_room(self.offices)
                    living_room = self.get_room(self.livingrooms)
                    # if there is no available office space
                    if work_room:
                        for room in self.offices:
                            if room.room_name == work_room:
                                room.occupants.append(person)
                                # update room capacity
                                room.room_capacity -= 1
                                print('A ' + person.occupation + ' ' + person.fname + ' has been added to ' + work_room)
                    else:
                        print('All offices are occupied, add a new office')
                    if living_room:
                        for room in self.livingrooms:
                            if room.room_name == living_room:
                                room.occupants.append(person)
                                # update room capacity
                                room.room_capacity -= 1
                                print('A ' + person.occupation + ' ' + person.fname + ' has been added to ' + living_room)
                    else:
                        print('All living rooms are occupied, add a new living room')
            else:
                print('A fellow with that name already exists')
        if occupation is 'Staff':
            person = Staff(fname=first_name, lname=last_name, occupation=occupation)
            self.all_people.append(person)
            self.staff.append(person)
            return 'A ' + person.occupation + ' ' + person.fname + person.lname + ' has been added successfully!'
