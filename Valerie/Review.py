class Review:
# reviews is an empty list so that it will be used to store all instances of reviews.
    reviews = [] 
    
    def __init__ (self, customer, restaurant, rating=None):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = None
         # Adding the review to the reviews list
        Review.reviews.append(self)  

        if rating is not None:
            self.set_rating(rating)
   
    # set_rating method allows rating only if the provided value is a number
    def set_rating(self, rating):
        if isinstance (rating,(int, float)):
            self._rating = rating
            
        else:
            print("Rating must be a number")
            
     # return the rating
    def get_rating(self):
        return self._rating   

    rating = property(get_rating, set_rating)
# returns customer object for that review
    def customer(self):
        return self._customer
# returns the restaurant object for that review
    def restaurant(self):
        return self._restaurant
            
    # the decorator @classmethod defines the class method/indicates that the method is a class
    #  the  method all() takes the class itself as the an argument(cls) method returns all reviews that have been created
    @classmethod
    def all(cls):
        return cls.reviews
    
    def __repr__(self):
        return f"{self._customer} ,{self._restaurant} {self._rating}"
    
# creating an instance of the review class
myreview = Review("Valerie", "Sippin serenade", 15)
newreview = Review("Kendy", "Del Ruiz", 14)

# getting the ratings of the reviews using the rating() method
print(myreview.rating)
print(newreview.rating)

# getting the customer reviews
print(myreview.customer())
print(newreview.customer())

# getting the restaurant reviews
print(myreview.restaurant())
print(newreview.restaurant())

# getting all the reviews
print(myreview)  
print(newreview)



        
        
        