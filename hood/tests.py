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
        self.lord_stark.save_profile(self.vikki)
