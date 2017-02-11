#from person import Person
from random import randint

class Room(object):

    """docstring for Room."""

    room_list = {}
    people_in_room_data = {}

    def __init__(self):
        pass

    def create_Rooms(self,room_name,room_category):

        """
        Creates a new room entry by ensuring that
        there are no duplicate entries,correct size and category

        """

        room = {}
        people ={}


        # Check if the room already exists in the room list

        if room_name in Room.room_list:

            print 'The Room already exists in the system'

        else:

            # Add room to app, only if it's 'OFFICE' or 'LIVING'

            if room_category.upper() == "OFFICE" or room_category.upper() == "LIVING":

                # Populate the room dictionary if the category is correct

                room['room_category'] = room_category.upper()
                room['room_name'] = room_name.upper()
                room['occupants'] = 0
                room['status'] = 'available'

                # people['room_name'] = room['room_name']
                # people['person_name'] = ''Room_in_room_data['person_name']''
                # people['employee_num'] = None

                room['people_in'] = Room.people_in_room_data

                if room_category == 'LIVING':

                    # Living rooms should have 4 occupants

                    room ['room_size']= 4

                elif room_category == 'OFFICE':

                    # Office rooms should have 6 occupants

                    room ['room_size'] = 6

            else:

                # Any other category is incorrect

                return 'Room type can only be LIVING or OFFICE '

        # Update the real time room list.

        Room.room_list[room_name] = room
        # Room.people_in_room_data[room_name] = people

        # Print Existing room list

        print Room.room_list

    def allocate_work_space(self):

        """"

        Allocates a room at random by filtering out office spaces
        that are available

        """

        # Check if room list contains available rooms.

        work_space_list =[]
        work_space_full =[]
        # people = {}
        work_space_number = None

        # Populating list with office spaces

        if len(Room.room_list) == 0:

            return 'There are no rooms added'

        else:

            # Traversing the list to determine that office spaces are available

            for work_space in Room.room_list:

                if Room.room_list[work_space]['room_category'] == 'OFFICE':

                    # Creating a list of available OFFICE spaces form a dictionary of all rooms

                    if Room.room_list[work_space]['room_category'] == \
                    'OFFICE'and Room.room_list[work_space]['occupants'] < 6:

                    # Appending data for list with work spaces to list

                        work_space_list.append(work_space)
                        #work_space_list.append(Roomself.people_in_room)

                    elif Room.room_list[work_space]['room_category'] ==\
                        'OFFICE' and Room.room_list[work_space]['occupants'] == 6:

                    # Collect all the full rooms
                        work_space_full.append(work_space)

                    else:

                        return 'No Office spaces in the system'

            if len(work_space_list)==0:

                return 'No more rooms'

            else:

                # Run a list index generator

                work_space_number = randint(0,len(work_space_list)-1)
                room_allocated = work_space_list[work_space_number]
                Room.room_list[room_allocated]['occupants'] += 1

                # Adding the specific person into the room that has been created
                # Every instance of this piece of code represents a record

                # people['person_name'] = person_name
                # people['room_name'] = room_allocated
                # people['employee_number'] = employee_number
                #
                # # Room.people_in_room_data['room_name'] = room_allocated
                # # Room.people_in_room_data['person_name'] = person_name
                # # Room.people_in_room_data['employee_number'] = employee_number
                #
                # Room.people_in_room_data[room_allocated] = people


        return work_space_list[work_space_number]

    def allocate_living_room(self):

        """"
        Allocates a room at random by filtering out Living spaces
        that are available

        """

        living_space_list = []
        living_space_full = []
        living_space_index = None

        if len(Room.room_list) == 0:

            return 'There are no rooms in the system'

        else:

            # Traversing the room list to find the living rooms available
            for living_space in Room.room_list:

                if Room.room_list[living_space]['room_category'] == 'LIVING':

                    # Creating a list of available Living Rooms

                    if Room.room_list[living_space]['room_category'] == \
                    'LIVING'and Room.room_list[living_space]['occupants'] < 4:

                    # Appending data for list with living spaces

                        living_space_list.append(living_space)

                    elif Room.room_list[living_space]['room_category'] ==\
                        'LIVING' and Room.room_list[living_space]['occupants'] == 4:

                    # Collect all the full rooms
                        living_space_full.append(living_space)

                    else:

                        return 'No Living spaces in the system'

            if len(living_space_list) == 0:

                return 'No Rooms Available'

            else:

                # Run an list index generator

                living_space_index = randint(0,len(living_space_list)-1)
                room_allocated = living_space_list[living_space_index]
                Room.room_list[room_allocated]['occupants'] += 1


        return living_space_list[living_space_index]

    def reallocate_room(self,employee_number,allocate_new):

        # Check if there are available rooms.
        if len(Room.room_list) == 0:

            return 'There are no rooms in the system'

        else:

            for reallocate_room in Room.room_list:


                if Room.room_list[work_space]['room_category'] == 'OFFICE':

                    # Creating a list of available spaces in the system

                    if Room.room_list[work_space]['room_category'] == \
                        'OFFICE' and Room.room_list[work_space]['occupants'] < 6:
                        allocated_room_list.append(reallocate_room)




        # Loading allocated rooms
        #loading available rooms
        # loading the people list



    def load_Rooms(self):

        # Open file with room data
        room_data = open('load_rooms.txt')

        ## Read the first line
        room_info = room_data.readline()

        while line:
            print line
            line = f.readline()
        f.close()

        return room_info


    def print_room(self):

        """Prints out the rooms that are available
         in the system

         """

        # Declaring a list of all avaialable rooms

        room_element = []

        # Looping through the room dictionary
        for room in Room.room_list:
            room_element.append(room)


        return room_element
