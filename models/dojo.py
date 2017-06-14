import sys
import random
from people import Staff, Fellow
from rooms import Office, LivingSpace
from os import path
from termcolor import colored
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

white_line = colored('-' * 60, 'white')


class Dojo(object):
    def __init__(self):
        self.offices = []
        self.livingrooms = []
        self.staff = []
        self.fellows = []
        self.all_rooms = []
        self.office_unallocated = []
        self.living_unallocated = []
        self.allocated = []
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
        # choose a room from the list of available rooms.
        chosen_room = random.choice(available_rooms)
        return chosen_room.room_name

    def create_room(self, room_name, room_type):
        """Creates a room in the system, either office or living space.
        :param room_name: A string representing a room's name.
        :param room_type: A string representing  a room's type (Office or Living space)
        """
        if room_type is 'office':
            if room_name not in [room.room_name for room in self.offices]:
                room = Office(room_name=room_name, room_type=room_type)
                self.offices.append(room)
                self.all_rooms.append(room)
                print(white_line)
                print(colored('An office called' + ' ' + room_name + ' ' + 'has been successfully created!', 'cyan'))
            else:
                print(white_line)
                print(colored('An office with that name already exists!', 'red'))
        if room_type is 'livingspace':
            if room_name not in [room.room_name for room in self.livingrooms]:
                room = LivingSpace(room_name=room_name, room_type=room_type)
                # add object to list( has both room_name and room_type)
                self.livingrooms.append(room)
                self.all_rooms.append(room)
                print(white_line)
                print(colored('An room called' + ' ' + room_name + ' ' + 'has been successfully created!', 'cyan'))
            else:
                print(white_line)
                print(colored('A living room with that name already exists!', 'red'))

    def add_person(self, first_name, last_name, occupation, wants_accommodation=None):
        """Adds person to the system and allocates them office space and room space if they
        are a fellow and requested for accommodation.
        :param first_name: A string representing the person's first name.
        :param last_name: A string representing the person's second name.
        :param occupation: A string representing the persons's   type (Fellow/Staff)
        :param wants_accommodation: An optional string representing a fellow's accommodation
        """

        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self. wants_accommodation = wants_accommodation
        self.person_name = self.first_name + self.last_name
        if occupation == 'Fellow':
            if self.person_name not in [person.fname + person.lname for person in self.fellows]:
                person = Fellow(first_name, last_name, occupation, wants_accommodation)
                self.fellows.append(person)
                print(white_line)
                print(colored(first_name + ' ' + last_name + ' has been added successfully!', 'cyan'))
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
                                print(white_line)
                                print(colored('A ' + person.occupation + ' '
                                      + person.fname + ' has been added to '
                                      + work_room, 'cyan'))
                    else:
                        # Add person to a list of unallocated if they got no office space.
                        self.office_unallocated.append(person)
                        print(white_line)
                        print(colored('All offices are occupied, added to office_unallocated list', 'red'))
                else:
                    # if a fellow does not want  accommodation then they get only office space
                    work_room = self.get_room(self.offices)
                    living_room = self.get_room(self.livingrooms)
                    # if there is no available office space
                    if work_room:
                        for room in self.offices:
                            if room.room_name == work_room:
                                room.occupants.append(person)
                                print(white_line)
                                print(colored('A ' + person.occupation + ' ' + person.fname +
                                      ' has been added to ' + work_room, 'cyan'))
                    else:
                        # Add person to a list of unallocated if they got no office space.
                        self.office_unallocated.append(person)
                        print(white_line)
                        print(colored('All offices are occupied, added to office_unallocated list', 'red'))
                    if living_room:
                        for room in self.livingrooms:
                            if room.room_name == living_room:
                                room.occupants.append(person)
                                print(white_line)
                                print(colored('A ' + person.occupation + ' ' + person.fname +
                                      ' has been added to ' + living_room, 'cyan'))
                    else:
                        # Add person to a list of unallocated if they got no office space.
                        self.living_unallocated.append(person)
                        print(white_line)
                        print(colored('All living rooms  are occupied, added to living_unallocated list', 'red'))
            else:
                print(white_line)
                print(colored('A fellow with that name already exists', 'red'))
        if occupation == 'Staff':
            if self.person_name not in [person.fname + person.lname for person in self.staff]:
                person = Staff(first_name, last_name, occupation)
                print(white_line)
                print(colored(first_name + ' ' + last_name + ' has been added successfully!', 'cyan'))
                self.staff.append(person)
                work_room = self.get_room(self.offices)
                if work_room:
                    for room in self.offices:
                        if room.room_name == work_room:
                            room.occupants.append(person)
                            print(white_line)
                            print(colored('A ' + person.occupation + ' ' + person.fname +
                                          ' has been added to ' + work_room, 'cyan'))
                else:
                    # Add person to a list of unallocated if they got no office space.
                    self.office_unallocated.append(person)
                    print(white_line)
                    print(colored('All offices are occupied, added to office_unallocated list', 'red'))
            else:
                print(white_line)
                print(colored('A member of staff with that name already exists!', 'red'))

    def print_room(self, room_name):
        """Gets a room name as an argument and returns a status of the room's
        existence and occupants if room exists
        :param room_name: A string representing  the name of the room.
        """
        # check if the requested room is available in the list of created rooms.
        if room_name not in [room.room_name for room in self.all_rooms]:
            print(white_line)
            print(colored('The room you entered is not in the system!', 'red'))
        for room in self.all_rooms:
            if room.room_name == room_name:
                print(room.room_name + '(' + room.room_type.title() + ')')
                print(white_line)
                print('Employee id' + '    ' + 'Employee Name')
                print(white_line)
                # check if room has occupants
                if room.occupants:
                    for person in room.occupants:
                        print(person.id + '           ' + person.fname + ' ' + person.lname)
                else:
                    print(colored('Room has currently no occupants!', 'red'))

    def print_allocation(self, filename):
        """Gets all the people in the dojo facility who have been awarded room and office allocations.
        """
        # writing to file
        write_to_file = ''
        for room in self.all_rooms:
            if room.occupants:
                print(colored(room.room_name + '(' + room.room_type.title() + ')', 'cyan'))
                write_to_file += room.room_name + '\n'
                print(white_line)
                for person in room.occupants:
                    person_name = person.fname + ' ' + person.lname
                    write_to_file += person_name + '\n'
                    print(person.id + ' ' + person_name)

                # check if user has opted to print list
                if filename:
                    file_name = filename + ".txt"
                    file_output = open(file_name, 'w')
                    file_output.write(write_to_file)
                    file_output.close()
                    return
            else:
                print(colored(room.room_name + '(' + room.room_type.title() + ')', 'cyan'))
                print(colored('This room has no occupants', 'red'))

    def print_unallocated(self, filename):
        # collect all file info as a string
        write_to_file = ''
        if self.office_unallocated:
            print(colored('Offices', 'cyan'))
            print(white_line)
            for person in self.office_unallocated:
                person_name = person.fname + ' ' + person.lname
                write_to_file += person_name + '\n'
                print(person.id + ' ' + person_name)
            # check if user has opted to print list
            if filename:
                file_name = filename + ".txt"
                file_output = open(file_name, 'w')
                file_output.write(write_to_file)
                file_output.close()
        if self.living_unallocated:
            print(colored('Living Rooms', 'cyan'))
            print(white_line)
            for person in self.living_unallocated:
                person_name = person.fname + ' ' + person.lname
                write_to_file += person_name + '\n'
                print(person.id + ' ' + person_name)
            # check if user has opted to print list
            if filename:
                file_name = filename + ".txt"
                file_output = open(file_name, 'w')
                file_output.write(write_to_file)
                file_output.close()

        else:
            print(white_line)
            print(colored('Currently no pending allocations!', 'cyan'))

    def get_current_room(self, person_id, room_type):
        for room in self.all_rooms:
            if room.room_type == room_type:
                for occupant in room.occupants:
                    if occupant.id == person_id:
                        return room
        return False

    def unallocate_person(self, person_id):
        """Removes a person from the room they are currently assigned to.
        :param person_id: A string representing the person's id.
        :return: person
        """
        for room in self.all_rooms:
            for occupant in room.occupants:
                if occupant.id == person_id:
                    person = occupant
                    room.occupants.remove(occupant)
                    return person

    def get_room_type(self, room_name):
        """Gets the room_type of the room to which reallocation is intended
        :param room_name:
        :return: room_type
        """
        for room in self.all_rooms:
            if room_name == room.room_name:
                if room.room_type == 'office':
                    return room.room_type, self.office_unallocated
                else:
                    return room.room_type, self.living_unallocated

    def reallocate_person(self, person_id, room_name):
        """Reallocates a person to a new room.
        :param person_id: A string representing a person's id.
        :param room_name: A string representing the name of the room to which reallocation is intended.
        """
        self.all_people = self.fellows + self.staff
        if room_name in [room.room_name for room in self.all_rooms]:
            for person in self.all_people:
                if person_id == person.id:
                    intended_room_type, unallocated = self.get_room_type(room_name)
                    current_room = self.get_current_room(person_id, intended_room_type)
                    if person not in unallocated:
                        for room in self.all_rooms:
                            if room_name == room.room_name:
                                if room.room_type == intended_room_type:
                                    if room_name != current_room.room_name:
                                        person = self.unallocate_person(person_id)
                                        room.occupants.append(person)
                                        print(white_line)
                                        return colored('reallocation successful!, new room: ' + room_name, 'cyan')
                                    else:
                                        return colored('Person already occupies that room!', 'red')
                                else:
                                    return colored('Reallocation for similar room_types only!', 'red')
                    else:
                        return colored('Only persons with rooms can be reallocated!', 'red')
            return colored('There is no person in the system with such an id!', 'red')
        else:
            return colored('The room specified does not exist!', 'red')

    def load_people(self, file_name):
        """Loads people from a text file
        :param file_name: A string representing the name of the file from which the loading should take place
        :return:
        """
        try:
            with open(file_name, 'r') as list_file:
                people = list_file.readlines()
                for person in people:
                    attributes = person.split()
                    if attributes:
                        first_name = attributes[0].title()
                        last_name = attributes[1].title()
                        occupation = attributes[2].title()
                        if len(attributes) == 4:
                            wants_accommodation = attributes[3]
                            self.add_person(first_name, last_name, occupation, wants_accommodation)
                        else:
                            self.add_person(first_name, last_name, occupation)
        except IOError:
            print(colored('There exists no file with such a name!'))
