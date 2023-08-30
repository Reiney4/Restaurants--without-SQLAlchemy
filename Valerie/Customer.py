#!/usr/bin/env python3

# Define a class Customer
class Customer:
    all_customers = []  # Class attribute to store all instances of Customer

    # Initialize a customer instance with given_name and family_name
    def __init__(self, given_name, family_name):
        # Convert given_name to string
        self.given_name = given_name
        # Convert family_name to string
        self.family_name = family_name 
        # Initialize full_name to None
        self.full_name = None
        # Call the set_full_name method to set the full_name
        self.set_full_name()
        # Add the instance to the list of all customers from self
        Customer.all_customers.append(self)

    # Set the given_name attribute
        def given_name(self):
            return self._given_name
        def family_name(self):
            return self._family_name
        
    
    # Combine given_name and family_name to set the full_name attribute
    def set_full_name(self):
        self.full_name = f"{self.given_name} {self.family_name}"    # Retrieve all customer instances
    @classmethod
    def all(cls):
        return cls.all_customers

# Creating instances of the Customer class
mycustomer = Customer("Valerie", "Kandagor")
newcustomer = Customer("Vicky", "Kendy")

# Retrieve all customers and print their full names
all_customers = Customer.all()
#used loop to get all the names to be combined
for customer in all_customers:
    print(customer.full_name)
