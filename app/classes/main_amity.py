
class Person(object):

    """docstring for Person."""

    def __init__(self):
        self.name=""
        pass
    def add_person(self):

        people_list=[]

        return people_list

    def load_people(self):
        people_list=[]

        return people_list

    def load_person(self):

        person_list=[]
        
        return person_list


class Fellow(object):

    """docstring for Fellow."""

    def __init__(self, arg):
        super(Fellow, self).__init__()
        self.arg = arg

    def request_office(self):
        pass

    def load_rooms(self):
        pass

    def request_living_space(self):
        pass

class Staff(object):

    """docstring for Staff."""

    def __init__(self, arg):
        super(Staff, self).__init__()
        self.arg = arg

class Room(object):

    """docstring for Room."""

    def __init__(self):
        self.name="Ed"
        self.roomcode="C400"
        self.category="LIVING"
        self.roomsize= 4
        pass

    def load_Rooms(self):
        pass

    def create_Rooms(self):
        #self.name=name
        pass

    def print_room(self):
        pass

    def reallocate_person(self):
        pass

class Office(object):

    """docstring for Office."""

    def __init__(self, arg):
        super(Office, self).__init__()
        self.arg = arg

    def allocate_office(arg):
        pass
    def unallocate_office(arg):
        pass

    def print_office(arg):
        pass


class LivingSpace(object):

    """docstring for LivingSpace."""

    def __init__(self, arg):
        super(LivingSpace, self).__init__()
        self.arg = arg
    def allocate_living_space(arg):
        pass
    def unallocate_living_space(arg):
        pass

    def print_living_space(arg):
        pass
