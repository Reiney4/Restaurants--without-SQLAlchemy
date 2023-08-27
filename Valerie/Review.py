#!/usr/bin/env python3

class Review:
    # Class attribute to store all instances of Review
    all_reviews = []

    def _init_(self, customer, restaurant, rating=None):
        # Initialize instance attributes
        self.customer = customer
        self.restaurant = restaurant
         # Initialize the private attribute _rating
        self._rating = None
          # Adding the review to the all_reviews list
        Review.all_reviews.append(self)
        if rating is not None:
            self.set_rating(rating)
            # used to retrieve the value of a property 
            def get_rating(self):
             return self._rating    
        
    #


    
