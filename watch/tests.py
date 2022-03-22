from django.test import TestCase
from .models import Business, Location, Profile, Neighborhood, Post
from django.contrib.auth.models import User

# Create your tests here.
class TestLocation(TestCase):
    def setUp(self):
      self.location = Location.objects.create(location='Machakos')

    def tearDown(self):
      Location.objects.all().delete()

   

    def test_save_location(self):
      self.location2 = Location.objects.create(location='Nairobi')
      self.assertEqual(len(Location.objects.all()), 2)
    
class TestNeighborhodd(TestCase):
  def setUp(self):
      self.location = Location.objects.create(location='Machakos')
      self.hood = Neighborhood.objects.create(name='Maanzoni', location=self.location, securityline=7, hospitalhelpline=7, occupants=8)

  def tearDown(self):
      Location.objects.all().delete()
      Neighborhood.objects.all().delete()

  def test_isinstance(self):
      self.assertTrue(isinstance(self.hood, Neighborhood))

  def test_deletehood(self):
      self.hood2 = Neighborhood.objects.create(name='Utawala', location=self.location, securityline= 5, hospitalhelpline=5, occupants=12)
      self.assertEqual(len(Neighborhood.objects.all()),2)
      Neighborhood.delete_neighborhood(self.hood.id)
      self.assertEqual(len(Neighborhood.objects.all()),1)

  def test_findneighborhood(self):
      searchterm = 'Utawala'
      self.hood2 = Neighborhood.objects.create(name='Utawala', location=self.location, securityline= 5, hospitalhelpline=5, occupants=12)
      results = Neighborhood.find_neighborhood(searchterm)
      self.assertTrue(len(results), 1)

  def test_updateneighbor(self):
      self.hood2 = Neighborhood.objects.create(name='Utawala', location=self.location, securityline= 5, hospitalhelpline=5, occupants=12)
      Neighborhood.update_neighborhood(self.hood2.id, name='Kitengela')
      updated = Neighborhood.objects.get(id = self.hood2.id)
      self.assertEqual(updated.name, 'Kitengela')


class TestProfile(TestCase):
    def setUp(self):
      self.newuser = User(username = "Mwongeli")
      self.newuser.save()
      self.location = Location.objects.create(location='Machakos')
      self.hood = Neighborhood.objects.create(name='Maanzoni', location=self.location, securityline=7, hospitalhelpline=7, occupants=8)
      self.newprofile = Profile.objects.create(profile_photo='test.jpg', bio='I code.', phone=2, location=self.location, neighborhood=self.hood )

    def tearDown(self):
      Profile.objects.all().delete()
      User.objects.all().delete()
      Neighborhood.objects.all().delete()
      Location.objects.all().delete

    def test_isinstance(self):
      self.assertTrue(isinstance(self.newprofile, Profile))  

      
class TestBusiness(TestCase):
    def setUp(self):
      self.location = Location.objects.create(location='Machakos')
      self.newuser = User.objects.create(username = 'Hoodie')
      self.hood = Neighborhood.objects.create(name='Maanzoni', location=self.location, securityline=7, hospitalhelpline=7, occupants=8)
      self.business = Business.objects.create(businessname = 'Vista', description='Description for Vista', username=self.newuser, neighborhood=self.hood)

    def tearDown(self):
      User.objects.all().delete()
      Neighborhood.objects.all().delete()
      Business.objects.all().delete()

    def test_isinstance(self):
      self.assertTrue(isinstance(self.business, Business))  

    def test_save_business(self):
      self.business2 = Business.objects.create(businessname = 'Mombasa Cement', description='Description for Mombasa Cement', username=self.newuser, neighborhood=self.hood)
      self.assertEqual(len(Business.objects.all()), 2)

    def test_delete_business(self):
      self.business2 = Business.objects.create(businessname = 'Mombasa Cement', description='Description for Mombasa Cement', username=self.newuser, neighborhood=self.hood)
      self.assertEqual(len(Business.objects.all()), 2)
      Business.delete_business(self.business2.id)
      self.assertEqual(len(Business.objects.all()), 1)

    def test_searchbusiness(self):
      self.business2 = Business.objects.create(businessname = 'Mombasa Cement', description='Description for Mombasa Cement', username=self.newuser, neighborhood=self.hood)
      searchterm = 'cement'
      searchresults = Business.searchbusiness(searchterm)
      self.assertEqual(len(searchresults), 1)
 

class Post(TestCase):
    def setUp(self):
      self.location = Location.objects.create(location='Machakos')
      self.hood = Neighborhood.objects.create(name='Maanzoni', location=self.location, securityline='1234567', hospitalhelpline='3456789', occupants=8)
      self.post = Post.objects.create(title='Thieves found.', story='We arrested the thieves who robbed house 52.', neighborhood=self.hood)

    def tearDown(self):
      Location.objects.all().delete()
      User.objects.all().delete()
      Neighborhood.objects.all().delete()
      Post.objects.all().delete

    def test_isinstance(self):
      self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
      self.post2 = Post.objects.create(title='Thieves found.', story='We arrested the thieves who robbed house 52.', neighborhood=self.hood)
      self.assertEqual(len(Post.objects.all()), 2)

    def test_delete_post(self):
      self.post2 = Post.objects.create(title='Thieves found.', story='We arrested the thieves who robbed house 52.', neighborhood=self.hood)
      self.assertEqual(len(Post.objects.all()), 2)
      Post.delete_post(self.post2.id)
      self.assertEqual(len(Post.objects.all()), 1)  
