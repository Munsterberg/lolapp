from django.test import TestCase
from .models import Scrim


class ScrimModelTest(TestCase):
    def test_string_representation(self):
        scrim = Scrim(team_name="TEST TEAM")
        self.assertEqual(str(scrim), scrim.team_name)
