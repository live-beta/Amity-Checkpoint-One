from room import Room
class Person(object):

    """docstring for Person."""
    people_list = {}

    def __init__(self):
        pass

    def add_person(self,person_name,person_job,wants_room ='N',emp_no):

        person = {}
        obj_room = Room()

        # Check if the person already exists in the people list

        if person_name and emp_no in Person.person_list:

            print 'The person already exists in the system'

        else:

            # Add person to app, only if they are 'STAFF' or 'FELLOW'

            if person_job.upper() == "FELLOW" or person_job.upper() == "STAFF":

                # Populate the person dictionary

                person['job'] = person_job.upper()
                person['name'] = person_name.upper()
                person['employee_num'] = emp_no
                person['job'] = person_job.upper()

                # Allocate working space to person
                person['work_space'] = obj_room.allocate_work_space()

                if wants_accommodation == 'Y' and person_job ='FELLOW':

                    # If Fellow wants accomodation

                    room_name = obj_room.allocate_living_room()

                    person['room'] = room_name.upper()

                elif wants_accommodation == 'Y' and person_job ='STAFF':

                    # An instance where Staff requests for accomodation

                    print 'Accomodation is only available for fellows'

                else:

                    # if fellow does not require accomodation

                    person['room'] = 'Unallocated'

            else:

                print 'Enter the correct job description'

        # Update the real time list.

        Person.people_list[emp_no] = person

        # Print people list

        return Person.people_list


    def allocate_work_space(self,emp_no):
        pass

class Fellow(person):

    """docstring for FELLOW, subclass of Person."""

    def __init__(self, arg):
        super(fellow, self).__init__()
        self.arg = arg

    def allocate_living_room(self,emp_no):
        pass


class Staff(person):

    """docstring for staff subclass of Person."""

    def __init__(self, arg):
        super(staff, self).__init__()
        self.arg = arg
