class Review:
    # Class attribute to store all instances of Review
    all_reviews = []

    def __init__(self, customer, restaurant, rating=None):
        # Initialize instance attributes
        self.customer = customer
        self.restaurant = restaurant
        # Initialize the private attribute _rating
        self._rating = None
        # Adding the review to the all_reviews list
        Review.all_reviews.append(self)
        if rating is not None:
            self.set_rating(rating)

    # Used to retrieve the value of the 'rating' property
    def get_rating(self):
        return self._rating

    # Used setter to ensure the rating is an integer
    def set_rating(self, rating):
        if isinstance(rating, int):
            self._rating = rating
        else:
            print("Rating must be an integer")

    # Create the 'rating' property using get_rating and set_rating methods
    rating = property(get_rating, set_rating)
