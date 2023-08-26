#created and initialized the class restaurant
class Restaurant:
    def __init__(self, name=None):
        self._name = None
        if name is not None:
            self.set_name(name)  # Using the setter here
    
   #