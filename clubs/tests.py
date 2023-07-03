from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Club


# Create your tests here.

class ThingTests(TestCase):

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