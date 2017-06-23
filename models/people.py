class Person(object):
    """Models the kind of people available at Andela,
    It forms the base class from which classes Fellow and Staff inherit"""

    person_id = 0
    staff_id = ''
    fellow_id = ''

    def __init__(self, first_name, last_name, occupation):
        """Initializes the base class Person
        :param first_name: A string denoting person's first name
        :param last_name: A string denoting a person's last name
        :param occupation: A string indicating whether a person is a Fellow or staff
        """
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.person_name = self.first_name + self.first_name

    def generate_person_id(self):
        """Generates a unique id for any person (Staff|Fellow) added to the system
        :return: fellow_id|staff_id: The id of the person to added.
        """
        if self.occupation is 'Fellow':
            Person.person_id += 1
            fellow_id = 'fel' + str(Person.person_id)
            return fellow_id
        elif self.occupation is 'Staff':
            Person.person_id += 1
            staff_id = 'stf' + str(Person.person_id)
            return staff_id
        else:
            return False


class Fellow(Person):
    def __init__(self, first_name, last_name, occupation, wants_accommodation='N', id=None, *args, **kwargs):
        super(Fellow, self).__init__(first_name, last_name, occupation='Fellow')
        self.wants_accommodation = wants_accommodation
        self.id = id or self.generate_person_id()


class Staff(Person):
    def __init__(self, first_name, last_name, occupation, wants_accommodation=None, id=None, *args, **kwargs):
        super(Staff, self).__init__(first_name, last_name, occupation='Staff')
        self.id = id or self.generate_person_id()
        self.wants_accommodation = wants_accommodation
