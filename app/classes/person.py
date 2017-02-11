import os
from room import Room

class Person(object):

    """docstring for Person."""
    people_list = {}
    room_allocation_list ={}

    def __init__(self):
        pass

    def add_person(self,person_name,person_job,wants_room,employee_number):
        """
        Function that adds a new person to the system

        """

        person = {}
        obj_room = Room()

        # Check if the person already exists in the people list

        if person_name in Person.people_list:

            print 'The person already exists in the system'

        else:

            # Add person to app, only if they are 'STAFF' or 'FELLOW'

            if person_job.upper() == "FELLOW" or person_job.upper() == "STAFF":

                # Populate the person dictionary

                person['job'] = person_job.upper()
                person['name'] = person_name.upper()
                person['employee_num'] = employee_number
                person['job'] = person_job.upper()

                # Allocate working space to person
                # work_space = obj_room.allocate_work_space()

                person['work_space'] = obj_room.allocate_work_space()

                if wants_room.upper() == 'Y' and person_job.upper() =='FELLOW':

                    # If Fellow wants accomodation

                    room_name = obj_room.allocate_living_room()

                    #work_space = obj_room.allocate_work_space()

                    person['room'] = room_name.upper()

                elif wants_room.upper() == 'Y' and person_job.upper() =='STAFF':

                    # An instance where Staff requests for accomodation

                    print 'Accomodation is only available for fellows'

                else:

                    # if fellow does not require accomodation

                    person['room'] = 'Unallocated'

            else:

                print 'Enter the correct job description'

        # Update the people list.

        Person.people_list[employee_number] = person

        # Print people list

        return Person.people_list

    def load_people(self):

        """
        Adding people from a text file on the users system

        """
        # Open file with people's data
        myfile = open("people.txt","r")
        data = ""
        lines = myfile.readlines()
        for line in lines:
            data = data + line.strip();

        return data

    def reallocate_person(self,emp_no,room_name):

        """
        Placing person in a different room.

        """
        personal_detail_list = {}
        # Loading data of an individual using a unique identifier employee number

        personal_detail_list = Person.people_list.get("employee_num",emp_no)

        # Assigning a new room to the person selected

        personal_detail_list['room'] = room_name

        #Updating the edited list

        Person.people_list.update(personal_detail_list)

        return Person.people_list

    def print_unallocated(self):

        """
        Prints out all the people who are unallocates in the system

        """
        unallocated_list = []
        return unallocated_list



class Fellow(Person):

    """docstring for FELLOW, subclass of Person."""

    def __init__(self, arg):
        super(fellow, self).__init__()
        self.arg = arg

    def allocate_living_room(self,emp_no):
        pass


class Staff(Person):

    """docstring for staff subclass of Person."""

    def __init__(self, arg):
        super(staff, self).__init__()
        self.arg = arg
