import os
import sys
import random
from os import path
from termcolor import colored
from people import Staff, Fellow
from rooms import Office, LivingSpace
from database.schema import People, DataBaseConnection, Rooms, Unallocated
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
        self.all_people = self.fellows + self.staff

    def get_room(self, rooms):
        """A function to generate a list of random rooms with space.
        :param rooms:
        :return: room_name
        """
        # a room is only available if it's capacity is not exceeded
        available_rooms = [room for room in rooms if len(room.occupants)
                           < room.room_capacity]
        # return False if all rooms are full
        if len(available_rooms) < 1:
            return False
        # choose a room from the list of available rooms.
        chosen_room = random.choice(available_rooms)
        return chosen_room.room_name

    def create_room(self, room_name, room_type):
        """Creates a room in the system, either office or living space.
        :param room_name: A string representing a room's name.
        :param room_type: A string representing  a room's type
        (Office or Living space)
        """
        if room_type is 'office':
            if room_name not in [room.room_name for room in self.offices]:
                room = Office(room_name=room_name, room_type=room_type)
                self.offices.append(room)
                self.all_rooms.append(room)
                print(white_line)
                print(colored('An office called' + ' ' + room_name + ' ' +
                              'has been successfully created!', 'cyan'))
            else:
                print(white_line)
                print(colored(
                    'An office with that name already exists!', 'red'))
        if room_type is 'livingspace':
            if room_name not in [room.room_name for room in self.livingrooms]:
                room = LivingSpace(room_name=room_name, room_type=room_type)
                # add object to list( has both room_name and room_type)
                self.livingrooms.append(room)
                self.all_rooms.append(room)
                print(white_line)
                print(colored('An room called' + ' ' + room_name + ' ' +
                              'has been successfully created!', 'cyan'))
            else:
                print(white_line)
                print(colored(
                    'A living room with that name already exists!', 'red'))

    def add_person(self, first_name, last_name,
                   occupation, wants_accommodation=None):
        """Adds person to the system and allocates them office space and
        room space if they are a fellow and requested for accommodation.
        :param first_name: A string representing the person's first name.
        :param last_name: A string representing the person's second name.
        :param occupation: A string representing
        the persons's type (Fellow/Staff)
        :param wants_accommodation: An optional string representing a
        fellow's accommodation
        """
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.wants_accommodation = wants_accommodation
        self.person_name = self.first_name + self.last_name
        if occupation == 'Fellow':
            if self.person_name not in [person.first_name + person.last_name
                                        for person in self.fellows]:
                person = Fellow(
                    first_name, last_name, occupation, wants_accommodation)
                print(colored(person.wants_accommodation, 'yellow'))
                self.fellows.append(person)
                print(white_line)
                print(colored(first_name + ' ' + last_name +
                              ' has been added successfully!', 'cyan'))
                # check if fellow wants accommodation,  set to 'N' by default
                accommodation = person.wants_accommodation
                if accommodation is None or accommodation != 'Y':
                    # if a fellow wants no accommodation grant just office
                    work_room = self.get_room(self.offices)
                    # if there is no available office space
                    if work_room:
                        for room in self.offices:
                            if room.room_name == work_room:
                                room.occupants.append(person)
                                print(white_line)
                                print(colored('A ' + person.occupation + ' '
                                      + person.first_name +
                                              ' has been added to '
                                      + work_room, 'cyan'))
                    else:
                        # Add person unallocated if no office space.
                        self.office_unallocated.append(person)
                        print(white_line)
                        print(colored('Office space unavailable, '
                                      'added to office waiting list', 'red'))
                else:
                    # Add person unallocated if no office space.
                    work_room = self.get_room(self.offices)
                    living_room = self.get_room(self.livingrooms)
                    # if there is no available office space
                    if work_room:
                        for room in self.offices:
                            if room.room_name == work_room:
                                room.occupants.append(person)
                                print(white_line)
                                print(colored('A ' + person.occupation +
                                              ' ' + person.first_name +
                                      ' has been added to '
                                              + work_room, 'cyan'))
                    else:
                        # Add person unallocated if no office space.
                        self.office_unallocated.append(person)
                        print(white_line)
                        print(colored('Office space unavailable, '
                                      'added to office waiting list', 'red'))
                    if living_room:
                        for room in self.livingrooms:
                            if room.room_name == living_room:
                                room.occupants.append(person)
                                print(white_line)
                                print(colored('A ' + person.occupation +
                                              ' ' + person.first_name +
                                      ' has been added to '
                                              + living_room, 'cyan'))
                    else:
                        # Add person unallocated if no office space.
                        self.living_unallocated.append(person)
                        print(white_line)
                        print(colored('Living space unavailable, '
                                      'added to accommodation waiting list',
                                      'red'))
            else:
                print(white_line)
                print(colored('A fellow with that name already exists',
                              'red'))
        # if occupation == 'Staff':
        #     if self.person_name not in [person.first_name + person.last_name
        #                                 for person in self.staff]:
        #         person = Staff(first_name, last_name, occupation, wants_accommodation=wants_accommodation)
        #         print(colored(person.wants_accommodation, 'yellow'))
        #         print(white_line)
        #         print(colored(first_name + ' ' + last_name +
        #                       ' has been added successfully!', 'cyan'))
        #         self.staff.append(person)
        #         work_room = self.get_room(self.offices)
        #         if work_room:
        #             for room in self.offices:
        #                 if room.room_name == work_room:
        #                     room.occupants.append(person)
        #                     print(white_line)
        #                     print(colored('A ' + person.occupation + ' ' +
        #                                   person.first_name +
        #                                   ' has been added to ' +
        #                                   work_room, 'cyan'))
        #         else:
        #             # Add person to a list of unallocated on missing office.
        #             self.office_unallocated.append(person)
        #             print(white_line)
        #             print(colored('Office space unavailable, '
        #                           'added to office waiting list', 'red'))
        #     else:
        #         print(white_line)
        #         print(colored('A member of staff with that '
        #                       'name already exists!', 'red'))
        if occupation == 'Staff':
            if self.person_name not in [person.first_name + person.last_name
                                        for person in self.staff]:
                person = Staff(
                    first_name, last_name, occupation, wants_accommodation)
                print(colored(person.wants_accommodation, 'yellow'))
                self.staff.append(person)
                print(white_line)
                print(colored(first_name + ' ' + last_name +
                              ' has been added successfully!', 'cyan'))
                accommodation = person.wants_accommodation
                if accommodation is None or accommodation != 'Y':
                    work_room = self.get_room(self.offices)
                    # if there is no available office space
                    if work_room:
                        for room in self.offices:
                            if room.room_name == work_room:
                                room.occupants.append(person)
                                print(white_line)
                                print(colored('A ' + person.occupation + ' '
                                      + person.first_name +
                                              ' has been added to '
                                      + work_room, 'cyan'))
                    else:
                        # Add person unallocated if no office space.
                        self.office_unallocated.append(person)
                        print(white_line)
                        print(colored('Office space unavailable, '
                                      'added to office waiting list', 'red'))
                else:
                    print(colored('Staff cannot get accommodation!', 'red'))
                    # Add person unallocated if no office space.
                    work_room = self.get_room(self.offices)
                    # if there is no available office space
                    if work_room:
                        for room in self.offices:
                            if room.room_name == work_room:
                                room.occupants.append(person)
                                print(white_line)
                                print(colored('A ' + person.occupation +
                                              ' ' + person.first_name +
                                      ' has been added to '
                                              + work_room, 'cyan'))
                    else:
                        # Add person unallocated if no office space.
                        self.office_unallocated.append(person)
                        print(white_line)
                        print(colored('Office space unavailable, '
                                      'added to office waiting list', 'red'))
            else:
                print(white_line)
                print(colored('A member of staff with that name already exists',
                              'red'))

    def print_room(self, room_name):
        """Gets a room name as an argument and returns a status of the room's
        existence and occupants if room exists
        :param room_name: A string representing  the name of the room.
        """
        # check if the requested room is available in created rooms.
        if room_name not in [room.room_name for room in self.all_rooms]:
            print(white_line)
            print(colored('The room you entered is not in the system!',
                          'red'))
        for room in self.all_rooms:
            if room.room_name == room_name:
                print(room.room_name + '(' + room.room_type.title() + ')')
                print(white_line)
                print('Employee id' + '    ' + 'Employee Name')
                print(white_line)
                # check if room has occupants
                if room.occupants:
                    for person in room.occupants:
                        print(person.id + '           ' +
                              person.first_name + ' ' + person.last_name)
                else:
                    print(colored('Room has currently no occupants!', 'red'))

    def print_allocation(self, filename):
        """Gets all the people in the dojo facility who have been awarded room
        and office allocations.
        """
        # writing to file
        write_to_file = ''
        for room in self.all_rooms:
            if room.occupants:
                print(colored(room.room_name +
                              '(' + room.room_type.title() + ')', 'cyan'))
                write_to_file += room.room_name + '\n'
                print(white_line)
                print('Employee id' + '    ' + 'Employee Name')
                print(white_line)
                for person in room.occupants:
                    person_name = person.first_name + ' ' + person.last_name
                    write_to_file += person_name + '\n'
                    print(person.id + '           ' + person.first_name +
                          ' ' + person.last_name)

                # check if user has opted to print list
                if filename:
                    file_name = filename + ".txt"
                    file_output = open(file_name, 'w')
                    file_output.write(write_to_file)
                    file_output.close()
                    return
            else:
                print(colored(room.room_name + '('
                              + room.room_type.title() + ')', 'cyan'))
                print(colored('This room has no occupants', 'red'))

    def print_unallocated(self, filename):
        # collect all file info as a string
        write_to_file = ''
        if self.office_unallocated:
            print(white_line)
            print(colored('OFFICES WAITING LIST', 'cyan'))
            print(white_line)
            print('Employee id' + '    ' + 'Employee Name')
            print(white_line)
            for person in self.office_unallocated:
                if person:
                    person_name = person.first_name + ' ' + person.last_name
                    write_to_file += person_name + '\n'
                    print(str(person.id) + '           ' +
                          person.first_name + ' ' +
                          person.last_name)
            # check if user has opted to print list
            if filename:
                file_name = filename + ".txt"
                file_output = open(file_name, 'w')
                file_output.write(write_to_file)
                file_output.close()
        if self.living_unallocated:
            print(white_line)
            print(colored('LIVING ROOMS WAITING LIST', 'cyan'))
            print(white_line)
            print('Employee id' + '    ' + 'Employee Name')
            print(white_line)
            for person in self.living_unallocated:
                person_name = person.first_name + ' ' + person.last_name
                write_to_file += person_name + '\n'
                print(str(person.id) + '           ' + person.first_name +
                      ' ' + person.last_name)
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
        return 'Person does not have a room of type {}'.format(room_type)

    def unallocate_person(self, person_id, intended_room_type):
        """Removes a person from the room they are currently assigned to.
        :param intended_room_type:
        :param person_id: A string representing the person's id.
        :return: person: The person to be reallocated.
        """
        for room in self.all_rooms:
            if room.room_type == intended_room_type:
                for occupant in room.occupants:
                    if occupant.id == person_id:
                        person = occupant
                        room.occupants.remove(occupant)
                        return person

    def get_room_type(self, room_name):
        """Gets the room_type of the room to which reallocation is intended
        :param room_name: The name of the room to reallocate to.
        :return: room_type: The name type of the room to reallocate
        """
        for room in self.all_rooms:
            if room_name == room.room_name:
                if room.room_type == 'office':
                    return room.room_type, self.office_unallocated
                else:
                    return room.room_type, self.living_unallocated

    @staticmethod
    def check_current_room_object(current_room):
        """Catches the error in current room to prevent passing of a
        string to function call in reallocate_person
        :param current_room: A string representing the room
        currently occupied by a person
        :return: boolean: This depends on whether current room
        is string or object.
        """
        try:
            if current_room.__dict__:
                return True
        except AttributeError:
            return False

    def reallocate_person(self, person_id, room_name):
        """Reallocates a person to a new room.
        :param person_id: A string representing a person's id.
        :param room_name: A string representing the name of the room to which
        reallocation is intended.
        """
        self.all_people = self.staff + self.fellows
        if room_name in [room.room_name for room in self.all_rooms]:
            for person in self.all_people:
                if person_id == person.id:
                    intended_room_type, unallocated =\
                        self.get_room_type(room_name)
                    current_room = self.get_current_room(person_id,
                                                         intended_room_type)
                    if person not in unallocated:
                        for room in self.all_rooms:
                            if room_name == room.room_name:
                                if room.room_type ==\
                                        intended_room_type \
                                        and len(room.occupants) \
                                        < room.room_capacity:
                                    if self.check_current_room_object(current_room):
                                        if room_name != current_room.room_name:
                                            person = self.unallocate_person(
                                                person_id, intended_room_type)
                                            room.occupants.append(person)
                                            print(white_line)
                                            return colored(
                                                'reallocation successful!,'
                                                'new room: ' +
                                                room_name, 'cyan')
                                        else:
                                            return colored(
                                                'Person already occupies that'
                                                ' room!', 'red')
                                    else:
                                        return colored(
                                            'Reallocation for similar '
                                            'room_types only!', 'red')
                                return colored('That room is fully occupied', 'red')
                    else:
                        return colored('Only persons with rooms can be '
                                       'reallocated!', 'red')
            return colored(
                'There is no person in the system with such an id!', 'red')
        else:
            return colored('The room specified does not exist!', 'red')

    def load_people(self, file_name):
        """Loads people from a text file
        :param file_name: A string representing the name of the file
        from which the loading should take place
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
                            self.add_person(first_name, last_name, occupation,
                                            wants_accommodation)
                        else:
                            self.add_person(first_name, last_name, occupation)
        except IOError:
            print(colored('There exists no file with such a name!'))

    def save_state(self, db_name=None):
        """Persists all the data stored in the app to a SQLite database.
        :param db_name: The name of the database to create.
        """
        if path.exists('default_amity_db.db'):
            os.remove('default_amity_db.db')
        if path.exists(str(db_name) + '.db'):
            os.remove(str(db_name) + '.db')
        if db_name is None:
            connection = DataBaseConnection()
        else:
            connection = DataBaseConnection(db_name)
        session = connection.Session()
        self.all_people = self.staff + self.fellows
        if self.all_people:
            print(colored('saving people to database.....', 'yellow'))
            for person in self.all_people:
                employee = People(
                    person.id, person.first_name, person.last_name,
                    person.occupation, person.wants_accommodation)
                session.add(employee)
                session.commit()
        else:
            print(colored('There are currently no people at the dojo!',
                          'red'))
        if self.all_rooms:
            print(colored('saving rooms to database....', 'yellow'))
            for room in self.all_rooms:
                room_occupants = ",".join([str(person.id) for person
                                           in room.occupants])
                space = Rooms(room.room_name, room.room_type,
                              room.room_capacity, room_occupants)
                session.add(space)
                session.commit()
        else:
            print(colored('There currently no rooms in the dojo!', 'red'))
        unallocated = self.office_unallocated + self.living_unallocated
        if unallocated:
            print(colored('saving unallocated to database....', 'yellow'))
            for person in self.office_unallocated:
                room_unallocated = 'Office'
                employee = Unallocated(person.id, person.first_name,
                                       person.last_name, person.occupation,
                                       room_unallocated)
                session.add(employee)
                session.commit()
            for person in self.living_unallocated:
                room_unallocated = 'Living space'
                employee = Unallocated(person.id, person.first_name,
                                       person.last_name, person.occupation,
                                       room_unallocated)
                session.add(employee)
                session.commit()
        else:
            print(colored('Currently there are no pending allocations!',
                          'cyan'))
        print('Data persisted to {} database successfully!'.
              format(connection.db_name))

    def load_state(self, db_name):
        """ Loads data from a database into the application.
        :param db_name: The name of the database from which to load the data.
        """
        connection = DataBaseConnection(db_name)
        session = connection.Session()
        saved_people = session.query(People).all()
        saved_rooms = session.query(Rooms).all()
        saved_unallocated = session.query(Unallocated).all()
        if saved_people:
            for person in saved_people:
                data = {'id': person.person_id,
                        'first_name': person.first_name,
                        'last_name': person.last_name,
                        'occupation': person.occupation,
                        'wants_accommodation': person.wants_accommodation}
                if person.occupation == 'Staff':
                    person = Staff(**data)
                    self.staff.append(person)
                if person.occupation == 'Fellow':
                    person = Fellow(**data)
                    self.fellows.append(person)
        else:
            print(colored('No saved people in the database', 'red'))
        if saved_rooms:
            self.all_people = self.staff + self.fellows
            for room in saved_rooms:
                if room.room_type == 'office':
                    if room.room_name \
                            not in [room.room_name for room in self.offices]:
                        space = Office(room.room_name, room.room_type)
                        occupants = [person_id for person_id in
                                     room.room_occupants.split(",")
                                     if person_id]
                        self.all_rooms.append(space)
                        if occupants:
                            for occupant in occupants:
                                person = self.get_person_object(
                                    occupant, self.all_people)
                                space.occupants.append(person)
                if room.room_type == 'livingspace':
                    if room.room_name \
                            not in [room.room_name for room in self.offices]:
                        space = LivingSpace(room.room_name, room.room_type)
                        occupants = [person_id for person_id in
                                     room.room_occupants.split(",") if person_id]
                        self.all_rooms.append(space)
                        if occupants:
                            for occupant in occupants:
                                person = self.get_person_object(occupant, self.all_people)
                                space.occupants.append(person)
            print(colored('Rooms successfully loaded.', 'cyan'))
        else:
            print(colored('No saved rooms in the database.', 'red'))
        if saved_unallocated:
            for person in saved_unallocated:
                if person.room_unallocated == 'Office' and\
                        person not in self.office_unallocated:
                        self.all_people = self.staff + self.fellows
                        person_object = self.get_person_object(
                            person.person_id, self.all_people)
                        self.office_unallocated.append(person_object)
                if person.room_unallocated == 'Living space' and\
                        person not in self.living_unallocated:
                        person_object = self.get_person_object(
                            person.person_id, self.fellows)
                        self.living_unallocated.append(person_object)
            print(colored('Unallocated people successfully loaded.', 'cyan'))
        else:
            print(colored(
                'No saved unallocated people in the database.', 'red'))

    @staticmethod
    def get_person_object(person_id, person_location):
        """Gets the person object for the person to be loaded from database
        :param person_id: the id of the person to be loaded
        :param person_location: The list of people where the person exists.
        :return: person: The person to be loaded.
        """
        for person in person_location:
            if person.id == person_id:
                return person








