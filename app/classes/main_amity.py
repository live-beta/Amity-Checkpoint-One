
from database import Database

class Person(object):

    """docstring for Person."""

    def __init__(self):
        self.name = None
        self.employee_num = None
        self.category = None
        self.wants_room = None
        self.is_allocated = None

    def add_person(self,name,employee_num,category,wants_room,is_allocated):

        # Instanciating the people variables

        people_list = {}
        new_person =[]

        new_person =[name,employee_num,category,ants_room,is_allocated]

        #Loding data that has been persisted to database

        people_list = self.Database.retrieve_people_info()

        # Appending the new person entered to the existing list

        people_list.update(new_person)


        return people_list

    def load_people(self):

        #Instanciating the people list dictionary

        load_people_list = {}

        # Reading people data from text_file.

        return load_people_list

    def load_person(self):

        person_list = {}

        return person_list

    def print_allocations(self):
        person_allocation_list ={}

        return person_allocation_list

    def print_unallocated(self):

        person_unallocated_list = {}

        return person_unallocated_list


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
        self.room_code=""
        self.category=""
        self.roomsize = None
        self.occupants = None

    def load_Rooms(self):
        pass

    def print_room(self):

        room_details={}

        return room_details


    def create_Rooms(self,name,category,room_code,size,occupants):

        # Instanciating room dictionary and new room list
        room_list ={}
        new_room=[]

        # Populating room from database

        room_list = self.Database.get_rooms()

        # Adding new room to list
        new_room = [name,category,room_code,size,occupants]

        # Appening the added list

        room_list.update{new_room}


        return room_list

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
