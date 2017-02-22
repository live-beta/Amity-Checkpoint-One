from room import Room
from person import  Person

class Office(Room):

    """docstring for Office."""

    def __init__(self, arg):
        super(Office, self).__init__()
        self.arg = arg

    def allocate_office_space(self,room_list,name,emp_no):

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
                        'LIVING' and \
                            Room.room_list[living_space]['occupants'] < 4:

                        # Appending data for list with living spaces

                        living_space_list.append(living_space)

                    elif Room.room_list[living_space]['room_category'] ==\
                        'LIVING' and \
                            Room.room_list[living_space]['occupants'] == 4:

                        # Collect all the full rooms
                        living_space_full.append(living_space)

                    else:

                        return 'No Living spaces in the system'

            if len(living_space_list) == 0:

                return 'No Rooms Available'

            else:

                # Run an list index generator
                living_space_index = randint(0, len(living_space_list)-1)
                room_allocated = living_space_list[living_space_index]
                Room.room_list[room_allocated]['occupants'] += 1

        return living_space_list[living_space_index]

    def reallocate_office(self,work_space):

        """
        Function to reallocate Office space on request from the users

        """



    def print_office_spaces(self):
        pass
