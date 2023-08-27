 #!/usr/bin/env python3

# Define a class Customer  
class Customer:
    all_customers = []  # Class attribute to store all instances of Customer
    
    # Initialize a customer instance with given_name and family_name
    def _init_(self, given_name, family_name):
        # Convert given_name to string
        self.given_name = str(given_name) 
         # Convert family_name to string 
        self.family_name = str(family_name)
        # Initialize full_name to None 
        self.full_name = None
        # Call the set_full_name method to set the full_name
        self.set_full_name()
        # Add the instance to the list of all customers from self
        Customer.all_customers.append(self)
        
    # Set the given_name attribute
    def set_given_name(self, given_name):
        if isinstance(given_name, str):
            self.given_name = str(given_name)
        else:
            print("Given name must be a string")

     # Set the family_name attribute
    def set_family_name(self, family_name):
        if isinstance(family_name, str):
            self.family_name = str(family_name)
        else:
            print("Family name must be a string")

    #  combine given_name and family_name to set the full_name attribute 
    def set_full_name(self):
        self.full_name = f"{self.given_name} {self.family_name}"

    # Retrieve all customer instances
    @classmethod
    def all(cls):
        return cls.all_customers