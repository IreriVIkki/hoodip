from django.test import TestCase
from datetime import datetime
# Create your tests here.
from .models import *

#  test categories class


class TestUser (TestCase):
    def setUp(self):
        self.vikki = User(username='vikki', password='akisijui')
        self.vikki.save()

    def tearDown(self):
        User.objects.all().delete()

    def test_instance(self):
        self.assertEqual(self.vikki.username, 'vikki')
        self.assertEqual(self.vikki.password, 'akisijui')
        self.assertTrue(isinstance(self.vikki, User))


class TestUserProfile (TestCase):
    def setUp(self):
        self.vikki = User(username='vikki', password='akisijui')
        self.vikki.save()
        self.lord_stark = Profile(user=self.vikki,
                                  user_name='Lord_stark', email='vikkicoder@gmail.com')

    def test_save_profile(self):
        self.lord_stark.save_profile(self.vikki)
        self.assertTrue(isinstance(self.lord_stark, Profile))


class TestBusiness(TestCase):
    def setUp(self):
        self.vikki = User.objects.create(username='vikki', password='akisijui')
        self.imara = NeighborHood.objects.create(
            admin=self.vikki, name='imara', location='Imara Daima', occupants=500000, address=30234)
        self.nyama = Business(
            name='nyama', email='nyama@gmail.com')
        self.nyama.save()

    def test_create_business(self):
        self.nyama.create_business(self.vikki, self.imara)
        self.assertTrue(isinstance(self.nyama, Business))
        self.assertTrue(self.nyama.owner, 'vikki')

    def test_delete_business(self):
        self.nyama.delete_business()
        self.assertTrue(self.nyama, None)

    def test_find_business(self):
        bs = Business.find_business(self.nyama.id)
        self.assertTrue(isinstance(bs, Business))

    def test_update_business(self):
        self.nyama.email = 'vikkicoder@gmail.com'
        self.nyama.update_business()
        self.assertTrue(self.nyama.email, 'vikkicoder@gmail.com')


class TestNeighborHood(TestCase):
    def setUp(self):
        self.vikki = User.objects.create(username='vikki', password='akisijui')
        self.imara = NeighborHood(
            name='imara', location='Imara Daima', occupants=500000, address=30234)
        self.imara.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.imara, NeighborHood))

    def test_create_neighborhood(self):
        self.imara.create_neigborhood(self.vikki)
        self.assertTrue(self.imara.admin, 'vikki')

    def test_delete_neighborhood(self):
        self.imara.delete_neigborhood()
        self.assertTrue(self.imara, None)

    def test_update_neighborhood(self):
        self.imara.name = 'Imara Daima'
        self.imara.update_neighborhood()
        self.assertTrue(self.imara.name, 'Imara Daima')
