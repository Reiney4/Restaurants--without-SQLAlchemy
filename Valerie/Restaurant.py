from review import Review

class Restaurant:
    def __init__(self,name=None):
        self._name = None
        if name is not None:
            self.set_name(name)
        
    def set_name (self,name):
        if isinstance (name,str):
            self._name = name
# returns the restaurant's name
    def name (self):
        return self._name
# returns a list of restaurant reviews
    def reviews(self):
        return[review for review in Review.all() if review.restaurant() ==self._name]
# returns a unique list of all customers who have reviewed a particular restaurant  
    def customers(self):
        return set([review.customer() for review in self.reviews()])
        
# calculate the average star rating
    def average_star_rating(self):
        if not self.reviews():
            return 0
        total_rating = sum(review.rating() for review in self.reviews())
        average = total_rating / len(self.reviews())
        return average 
     
restaurant1 = Restaurant("Sippin serenade")   
print(restaurant1.name())

    