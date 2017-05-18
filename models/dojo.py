import sys
import random
from people import Staff, Fellow
from rooms import Office, LivingSpace
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class Dojo(object):
    def __init__(self):
        self.offices = []
        self.livingrooms = []
        self.staff = []
        self.fellows = []
        self.all_rooms = []
        self.all_people = []
        self.unallocated = []

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
        # choose a room from the list of available rooms.
        chosen_room = random.choice(available_rooms)
        return chosen_room.room_name

    def create_room(self, room_name, room_type):
        """Creates a room in the system, either office or living space.
        :param room_name: A string representing a room's name.
        :param room_type: A string representing  a room's type (Office or Living space)
        :return:
        """
        if room_type is 'office':
            if room_name not in [room.room_name for room in self.offices]:
                room = Office(room_name=room_name, room_type=room_type)
                self.offices.append(room)
                self.all_rooms.append(room)
                print('An office called' + ' ' + room_name + ' ' + 'has been successfully created')
            else:
                print('An office with that name already exists')
        if room_type is 'livingspace':
            if room_name not in [room.room_name for room in self.livingrooms]:
                room = LivingSpace(room_name=room_name, room_type=room_type)
                # add object to list( has both room_name and room_type)
                self.livingrooms.append(room)
                self.all_rooms.append(room)
                print('A room called ' + room_name + ' has been successfully created!')
            else:
                print('A living room with that name already exists')

    def add_person(self, first_name, last_name, occupation, wants_accommodation=None):
        """Adds person to the system and allocates them office space and room space if they
        are a fellow and requested for accommodation.
        :param first_name: A string representing the person's first name.
        :param last_name: A string representing the person's second name.
        :param occupation: A string representing the persons's   type (Fellow/Staff)
        :param wants_accommodation: An optional string representing a fellow's accomodation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self. wants_accommodation = wants_accommodation
        self.person_name = self.first_name + self.last_name
        if occupation is 'Fellow':
            if self.person_name not in [person.fname + person.lname for person in self.fellows]:
                person = Fellow(first_name, last_name, occupation, wants_accommodation)
                self.fellows.append(person)
                print(first_name + ' ' + last_name + ' has been added successfully!')
                # check if fellow wants accommodation, it is set to 'N' by default
                accommodation = person.wants_accommodation
                if accommodation is None:
                    # if a fellow does not want  accommodation then they get only office space
                    work_room = self.get_room(self.offices)
                    # if there is no available office space
                    if work_room:
                        for room in self.offices:
                            if room.room_name == work_room:
                                room.occupants.append(person)
                                print('A ' + person.occupation + ' ' + person.fname + ' has been added to ' + work_room)
                    else:
                        # Add person to a list of unallocated if they got no office space.
                        self.unallocated.append(person)
                        print('All offices are occupied, you will be added once space is available')
                else:
                    # if a fellow does not want  accommodation then they get only office space
                    work_room = self.get_room(self.offices)
                    living_room = self.get_room(self.livingrooms)
                    # if there is no available office space
                    if work_room:
                        for room in self.offices:
                            if room.room_name == work_room:
                                room.occupants.append(person)
                                print('A ' + person.occupation + ' ' + person.fname + ' has been added to ' + work_room)
                    else:
                        # Add person to a list of unallocated if they got no office space.
                        self.unallocated.append(person)
                        print('All offices are occupied, you will be added once space is available')
                    if living_room:
                        for room in self.livingrooms:
                            if room.room_name == living_room:
                                room.occupants.append(person)
                                print('A ' + person.occupation + ' ' + person.fname + ' has been added to ' + living_room)
                    else:
                        # Add person to a list of unallocated if they got no office space.
                        self.unallocated.append(person)
                        print('All living rooms  are occupied, you will be added once space is available')
            else:
                print('A fellow with that name already exists')
        if occupation is 'Staff':
            if self.person_name not in [person.fname + person.lname for person in self.staff]:
                person = Staff(first_name, last_name, occupation)
                print(first_name + ' ' + last_name + ' has been added successfully!')
                self.staff.append(person)
                work_room = self.get_room(self.offices)
                if work_room:
                    for room in self.offices:
                        if room.room_name == work_room:
                            room.occupants.append(person)
                            print('A ' + person.occupation + ' ' + person.fname + ' has been added to ' + work_room)
                else:
                    # Add person to a list of unallocated if they got no office space.
                    self.unallocated.append(person)
                    print('All offices are occupied, you will be added once space is available')
            else:
                print('A member of staff with that name already exists')

    def print_room(self, room_name):
        """Gets a room name as an argument and returns a status of the room's
        existence and occupants if room exists
        :param room_name: A string representing  the name of the room.
        """
        # check if the requested room is available in the list of created rooms.
        if room_name not in [room.room_name for room in self.all_rooms]:
            print('The room you entered is not in the system')
        for room in self.all_rooms:
            if room.room_name == room_name:
                print(room.room_name)
                print('-' * 100)
                # check if room has occupants
                if room.occupants:
                    print(room.room_name)
                    for person in room.occupants:
                        print(person.fname + ' ' + person.lname)
                else:
                    print('Room has currently no occupants')

    def print_allocation(self, filename):
        """Gets all the people in the dojo facility who have been awarded room and office allocations.
        """
        # writing to file
        write_to_file = ''
        for room in self.all_rooms:
            if room.occupants:
                print(room.room_name)
                write_to_file += room.room_name + '\n'
                print('_' * 100)
                for person in room.occupants:
                    person_name = person.fname + ' ' + person.lname
                    write_to_file += person_name + '\n'
                    print(person_name)
                print('-' * 100)
        file_name = "" + filename + ".txt"
        file_output = open(file_name, 'w')
        file_output.write(write_to_file)
        file_output.close()

    def print_unallocated(self, filename):
        print('-' * 100)
        # collect all file info as a string
        write_to_file = ''
        if self.unallocated:
            for person in self.unallocated:
                person_name = person.fname + ' ' + person.lname
                write_to_file += person_name + '\n'
                print(person_name)
            file_name = "" + filename + ".txt"
            file_output = open(file_name, 'w')
            file_output.write(write_to_file)
            file_output.close()

        else:
            print('All Allocations have taken place')
