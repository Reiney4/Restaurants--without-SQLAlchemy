import unittest
from Restaurant import Restaurant  
from Review import Review  
from Customer import Customer
class TestRestaurantMethods(unittest.TestCase):

    def setUp(self):
        self.restaurant1 = Restaurant('Sippin serenade')

    def test_name(self):
        self.assertEqual(self.restaurant1.name(), 'Sippin serenade')


    def test_average_star_rating_with_reviews(self):
        # Create some review instances
        Review.reviews = []  # Clear existing reviews
        
        myreview = Review("Valerie", "Sippin serenade", 12)
        newreview = Review("Kendy", "Del Ruiz", 10)
        self.assertEqual(self.restaurant1.average_star_rating(), (12 + 10) / 2)
    
    def test_customers_with_reviews(self):
        Review.reviews = []  # Clear existing reviews
        
        myreview = Review("Valerie", "Sippin serenade", 12)
        newreview = Review("Kendy", "Del Ruiz", 10)
        
        expected_customers = {"Valerie", "Kanadagor"}
        self.assertEqual(self.restaurant1.customers(), expected_customers)
    def test_reviews_with_matching_restaurant(self):
        # Create some review instances
        Review.reviews = [] 
        
        myreview = Review("Valerie", "Sippin serenade", 12)
        newreview = Review("Kendy", "Del Ruiz", 10)
        other_review = Review("Some Customer", "orthega", 9)
        
        self.assertEqual(self.restaurant1.reviews(), [myreview, newreview])

    def test_reviews_with_non_matching_restaurant(self):
        # Create some review instances
        Review.reviews = []  
        
        myreview = Review("Valerie", "Sippin serenade", 12)
        newreview = Review("Kendy", "DEl Ruiz", 10)
        
        self.assertEqual(self.restaurant1.reviews(), [])
        
class TestCustomerMethods(unittest.TestCase):

    def setUp(self):
        self.mycustomer = Customer("Valerie", "Kendy")
        self.newcustomer = Customer("Valerie", "Kandagor")
     
        
    def test_given_name(self):
        self.assertEqual(self.mycustomer.given_name, "Valerie")
        self.mycustomer.given_name = "NewValerie"
        self.assertEqual(self.mycustomer.given_name, "NewValerie")

    def test_family_name(self):
        self.assertEqual(self.mycustomer.family_name, "Kendy")
        self.mycustomer.family_name = "NewKendy"
        self.assertEqual(self.mycustomer.family_name, "NewKendy")

    def test_full_name(self):
        self.assertEqual(self.mycustomer.full_name(), "Mercy Kendy")

    def test_find_all_by_given_name(self):
        # Test finding all customers by a given name
        all_mycustomers = Customer.find_all_by_given_name("Valerie")
        self.assertEqual(len(all_mycustomers), 11)
        for customer in all_mycustomers:
            self.assertEqual(customer.given_name, "Valerie")

    
    def test_add_review(self):
        Review.reviews = []  
        
        self.mycustomer.add_review("orthega", 8)
        self.assertEqual(self.mycustomer.num_reviews(), 1)
        self.assertEqual(len(Review.all()), 1)

    def test_find_by_name_existing(self):
        self.assertEqual(Customer.find_by_name("Valerie Kandagor"), self.mycustomer)

    def test_find_by_name_non_existing(self):
        self.assertIsNone(Customer.find_by_name("Vicky"))

   
    def test_find_by_name_existing(self):
        found_customer = Customer.find_by_name("Valerie Kendy")
        self.assertEqual(found_customer.given_name, "Valerie")
        self.assertEqual(found_customer.family_name, "Kendy")
        
    def test_all_customers(self):
        # Create some customer instances
        customer1 = Customer("Caren", "Nyigei")
        customer2 = Customer("Sharon", "Koech")
        customer3 = Customer("Kylie", "Cloy")
        
        # Call the all class method
        all_customers = Customer.all()
        
        # Verify that all created customers are in the list
        self.assertIn(customer1, all_customers)
        self.assertIn(customer2, all_customers)
        self.assertIn(customer3, all_customers)    
        
class TestReviewMethods(unittest.TestCase):

    def setUp(self):
        myreview = Review("Valerie", "Sippin serenade", 12)
        newreview = Review("Kendy", "Del Ruiz", 10)
    def test_rating(self):
        self.assertEqual(self.myreview.rating(), 12)
        self.assertEqual(self.newreview.rating(), 10)
       
    def test_customer(self):
        self.assertEqual(self.myreview.customer(), "Valerie")
        self.assertEqual(self.newreview.customer(), "Kandagor")

    def test_restaurant(self):
        self.assertEqual(self.good_review.restaurant(), "Sippin serenade")
        self.assertEqual(self.bad_review.restaurant(), "Del Ruiz")

    def test_all(self):
        all_reviews = Review.all()
        self.assertIn(self.myreview, all_reviews)
        self.assertIn(self.newreview, all_reviews)
        
    # Add more test cases here for other methods if needed



if __name__ == '__main__':
    unittest.main()