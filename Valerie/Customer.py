#!/usr/bin/env python3

# Assuming Review class is defined elsewhere
class Review:
    @staticmethod
    def all():
        pass
  # Implement this method to return all reviews

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._full_name = f"{given_name} {family_name}"
        self.set_full_name()
        Customer.all_customers.append(self)

    def set_given_name(self, given_name):
        if isinstance(given_name, str):
            print(f"Setting given name to: {given_name}")
            self._given_name = given_name
            self.set_full_name()
        else:
            print('Given name must be a string.')

    def get_given_name(self):
         return self._given_name

    given_name = property(get_given_name, set_given_name)

    def set_family_name(self, family_name):
        if isinstance(family_name, str):
            print(f"Setting family name to: {family_name}")
            self._family_name = family_name
            self.set_full_name()
        else:
            print('Family name must be a string.')

    def get_family_name(self):
        return self._family_name

    family_name = property(get_family_name, set_family_name)

    def set_full_name(self):
        self._full_name = f"{self._given_name} {self._family_name}"

    @property
    def full_name(self):
        return self._full_name

    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants(self):
        return set([review.restaurant() for review in Review.all() if review.customer() == self.full_name])

    def add_review(self, restaurant, rating):
         # Assuming the Review class constructor accepts these arguments
        Review(self.full_name, restaurant, rating) 

    def num_reviews(self):
        reviews = [review for review in Review.all() if review.customer() == self.full_name]
        return len(reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name == name:
                return customer
            # Moved print statement outside the loop

        print("Customer not found")  
    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name == name]

# Creating instances of the Customer class
my_customer = Customer("Valerie", "Kandagor")
new_customer = Customer("Vicky", "Kendy")

# Retrieve all customers and print their full names
all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name)
