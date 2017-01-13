
class Person():
    """docstring for Person."""
    def __init__(self):
        pass
    def add_person(name,gender,category,employee_num):
        pass

class Fellow(object):
    """docstring for Fellow."""
    def __init__(self, arg):
        super(Fellow, self).__init__()
        self.arg = arg

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
    def create_Rooms(self,roomcode,name,size,category):
        #self.name=name

        pass

class Office(object):
    """docstring for Office."""
    def __init__(self, arg):
        super(Office, self).__init__()
        self.arg = arg

class LivingSpace(object):
    """docstring for LivingSpace."""
    def __init__(self, arg):
        super(LivingSpace, self).__init__()
        self.arg = arg
