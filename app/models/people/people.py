class Person(object):
    """Models the kind of people available at Andela,
    It forms the base class from which classes Fellow and Staff inherit"""

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
