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

    
    
# Create an instance of the Restaurant class
restaurant = Restaurant("Sippin Serenade")
print(restaurant.name())  

# name cannot be changed
restaurant.name("Del Ruiz")
print(restaurant.name()) 
