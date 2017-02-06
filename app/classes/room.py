
class Room(object):

    """docstring for Room."""

    room_list={}

    def __init__(self):
        self.name="Ed"
        #self.room_code=""
        self.category=""
        self.roomsize = None
        self.occupants = None

    def create_Rooms(self,room_name,room_category):

        """Creates a new room entry by ensuring that
            there are no duplicate entries,correct size and category
        """

        room = {}

        # Check if the room already exists in the room list

        if room_name in Room.room_list:

            print 'The Room already exists in the system'

        else:

            # Add room to app, only if it's 'OFFICE' or 'LIVING'

            if room_category.upper() == "OFFICE" or \
                room_category.upper() == "LIVING":

                # Populate the room dictionary if the category is correct

                room['room_category'] = room_category.upper()
                room['room_name'] = room_name.upper()

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

        # Print Existing room list

        return Room.room_list

    def allocate_work_space(self):

        """"
        Allocates a room at random by filtering out office spaces
        that are available
        """"

        # Check if room list contains available rooms.

        work_space_list =[]
 
        # Populating list with office spaces

        for space in room_list:

            # Check if the office spaces are fully occupied

            if category == "OFFICE" and occupants < 6 :

                work_space_list.append(space)

            elif space.occupants == 6:

                return 'All Spaces are occupied'

        # When there are no rooms in the list

        if len(work_space_list) == 0:

            return 'Office spaces not available '

        else:

            # Random room allocation

            work_space_number = randint(0,len(work_space_list))

        # Returning room from list

        return work_space_list[work_space_number]


    def allocate_living_room(self):
        """"
        Allocates a room at random by filtering out Living spaces
        that are available
        """"

        living_space_list = []

        # Populating lis with living spaces

        for living_space in room_list:

            # Check is the rooms are fully occupied

            if category == "LIVING" and occupants < 4:

                living_space_list.append(living_space)

            elif living_space.occupants == 6:

                return 'All Occupied'

        # If there are no rooms returned

        if len(living_space_list) == 0:

            return 'No Spaces To Allocate'
        else:
            # Allocate the available rooms randomly
            living_space_number =randint(0, len(living_space_list))

        return living_space_list[living_space_number]

    def load_Rooms(self):
        pass

    def print_room(self):

        room_details={}

        return room_details