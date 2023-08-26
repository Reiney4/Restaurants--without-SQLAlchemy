#created and initialized the class restaurant
class Restaurant:
    def __init__(self, name=None):
        self._name = None
        if name is not None:
            self.set_name(name)  
    
    # Using the setter here to set name
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            print("Name must a string!")
    
# Create an instance of the Restaurant class
restaurant = Restaurant("Sippin Serenade")

# Accessing the name using the getter
print(restaurant.get_name())  

# Using the setter to change the name
restaurant.set_name("Del Ruiz")
print(restaurant.get_name()) 
