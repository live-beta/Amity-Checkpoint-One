

from database import Database
from app_data import Add_Data

class Amity(object):

    """docstring for Amity."""

    person_info_dict = {}

    def __init__(self):
        super(Amity, self).__init__()
        self.name= None
        self.employee_num = ''
        self.category = None
        self.is_allocated =None
        self.room_name = ''
        self.room_category= None
        self.room_size = None
        self.room_occupants = None
        self.person_dict = {}
        self.empno = 0


    def add_person(self,person_name,person_job,wants_room,emp_no):

        "Function that adds a new FELLOW or STAFF to the application"

        # Instaninating the people variables

        #person_dict = {}
        new_person = []

        #new_person= [name,category,wants_room]
        # index = self.empno

        if len(self.person_dict) == 0:

            if person_job.upper() == "FELLOW" or person_job.upper() == "STAFF":

                self.person_dict['job']= person_job.upper()
                self.person_dict['name'] = person_name.upper()
                self.person_dict['employee_num'] = emp_no
                self.person_dict['job']= person_job.upper()

            else:

                print 'The job description is not correct'
        else:
            if person_job.upper() == "FELLOW" or person_job.upper() == "STAFF":

                self.person_dict['job'].update(person_job.upper())
                self.person_dict['name'].update (person_name.upper())
                self.person_dict['employee_num'].update(emp_no)
                self.person_dict['job'].update(person_job.upper())

            else:

                print 'The job description is not correct'



        # Loading data that has been persisted in database

        #people_list = self.Database.retrieve_people_info()

        # Appending  the new person, to the exestin list.

    #   people_list= self.Database.retrieve_people_info()

        # Appending the new person entered to the exesting list

        #people_list.update(new_person)
        # obj_app_data = Add_Data()
        # obj_app_data.people_info.update(self.person_dict)

        Amity.person_info_dict[emp_no] =self.person_dict

        print Amity.person_info_dict


        #return person_dict


    def create_Rooms(self,room_name,category):

        # Instanciating room dictionary and new room list
        room_list ={}
        new_room=[]

        # Populating room from database/from application data

        room_list = self.Database.get_rooms()

        # Adding new room to list
        new_room = [room_name]

        # Appening the added list

        room_list.update(new_room)

        #Returnin the room list

        return room_list

    def reallocate_person(self):

        # Instanciating fvariables
        peron_room_allocaion = []
        room_realocations = {}

        # Loadinng room allocation data dictionary sorted by employee_num
        person_room_allocation = self.Database.get_allocation()

        # Editing the room entry in the list
        room_index = personal_room_allocation.index(room)
        personal_room_allocation[room_index] = room_name

        # Returning the updated list

        return personal_room_allocation

    def load_people(self):

        #Instanciating the people list dictionarys

        load_people_list = {}
        fellow_record = []


        fellow_information = open("fellows.txt","r")

        # Looping through the various text_file lines to extract fellow information

        for line in file:

          # Splitting the lines and assigning each to a fellow record and adding to dictionary

          fellow_record[record_id] = line.split(";")
          load_people_list.update(fellow_record)

        file.close()

        # Returning the information from text_file

        return load_people_list

    def load_person(self):

        # Instance of finding and loading one person into the list
        person_data ={}

        return person_data

    def print_unallocated(self):

        "Prints  a list of unallocated people to the screeen"

        # Loading data for unallocated individuals

        load_unallocated ={}

        # Writing the unallocated into a text file.


        return load_unallocated


    def print_allocations(self):

        "Printing out amity allocation details"

        person_allocation_list ={}

        return person_allocation_list


    def print_room(self):

        # Room dictionary for amity

        amity_rooms = {}

        return amity_rooms

    def load_state(self):

        pass

    def save_state(self):
        pass

class app_data(object):

    """docstring for  loading data."""

    def __init__(self, arg):
        super(save_app_data, self).__init__()
        self.arg = arg

    def load_data(self):

        "Function for loading information for the application"

        # Defining the various dictionaries


        pass
