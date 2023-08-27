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
        Customer.all_customers.append(self)  # Add the instance to the list of all customers
        
    # Set the given_name attribute
   #