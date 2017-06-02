class Person(object):
    """Models the kind of people available at Andela,
    It forms the base class from which classes Fellow and Staff inherit"""

    person_id = 0
    staff_id = ''
    fellow_id = ''

    def __init__(self, fname, lname, occupation):
        """Initializes the base class Person
        :param fname: A string denoting person's first name
        :param lname: A string denoting a person's last name
        :param occupation: A string indicating whether a person is a Fellow or staff
        """
        self.fname = fname
        self.lname = lname
        self.occupation = occupation
        self.person_name = self.fname + self.fname

    def generate_person_id(self):
        """Generates a unique id for any person (Staff|Fellow) added to the system
        :return: fellow_id|person_id
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
    def __init__(self, fname, lname, occupation, wants_accommodation='N'):
        super(Fellow, self).__init__(fname, lname, occupation='Fellow')
        self.wants_accommodation = wants_accommodation
        self.id = self.generate_person_id()


class Staff(Person):
    def __init__(self, fname, lname, occupation):
        super(Staff, self).__init__(fname, lname, occupation='Staff')
        self.id = self.generate_person_id()

