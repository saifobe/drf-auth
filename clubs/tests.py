from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Club


# Create your tests here.

class ClubsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_thing = Club.objects.create(name='flower', fan=testuser1, club_wiki="test desc ...")
        test_thing.save()

    def club_model(self):
        club = Club.objects.get(id=1)
        actual_fan= str(club.fan)
        actual_name = str(club.name)
        actual_club_wiki = str(club.club_wiki)
        self.assertEqual(actual_fan,"testuser1")
        self.assertEqual(actual_name,"flower")
        self.assertEqual(actual_club_wiki,"test desc ...")

    def test_club_content(self):
        club = Club.objects.get(id=1)
        expected_fan= f'{club.fan}'
        expected_name = f'{club.name}'
        expected_club_wiki = f'{club.club_wiki}'
        self.assertEqual(expected_fan, 'testuser1')
        self.assertEqual(expected_name, 'flower')
        self.assertEqual(expected_club_wiki, 'test desc ...')
