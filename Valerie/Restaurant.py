#  
    
    # Using the setter here to set name
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Name must a string!")
    
#