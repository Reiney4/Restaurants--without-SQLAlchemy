#created and initialized the class restaurant
class Restaurant:
    def __init__(self, name):
        #sets to private  remove none
        self._name = name
        
    # Using the getter here to set name shd not change or @property
    def name(self):
        return self._name
    
    #a list of reviews should be returned
    def reviews(self):
        return [review for review in Review.all() if review.restaurant()== self._name]
    
    #a list of customersshould be returned
    def customers(self):
        return set([review.customer() for review in  self.reviews()] )

    #calculate the average string
    def average_star_rating(self):
        if not self.reviews():
            return 0  # No reviews, so average is 0
        total_ratings = sum(review.rating() for review in self.reviews())
        average = total_ratings / len(self.reviews())
        return average
    
# Create an instance of the Restaurant class
restaurant = Restaurant("Sippin Serenade")
print(restaurant.name())  

# name cannot be changed
restaurant.name("Del Ruiz")
print(restaurant.name()) 
