#!/usr/bin/python3
import unittest
import models
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os


# skip these test if the storage is not db
@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip if not fs")
class TestDBStorage(unittest.TestCase):
    """DB Storage test"""

    def setUp(self):
        """ Set up test environment """
        self.storage = models.storage

    def tearDown(self):
        """ Remove storage file at end of tests """
        del self.storage

    def test_user(self):
        """ Tests user """
        user = User(name="Chyna", email="chyna@gmail.com", password="Chyna12345")
        user.save()
        self.assertFalse(user.id in self.storage.all())
        self.assertEqual(user.name, "Chyna")

    def test_city(self):
        """ test city """
        state = State(name="California")
        state.save()
        city = City(name="Batch")
        city.state_id = state.id
        city.save()
        self.assertFalse(city.id in self.storage.all())
        self.assertEqual(city.name, "Batch")

    def test_state(self):
        """ test state"""
        state = State(name="California")
        state.save()
        self.assertFalse(state.id in self.storage.all())
        self.assertEqual(state.name, "California")

    def test_place(self):
        """Test place"""
        state = State(name="California")
        state.save()
