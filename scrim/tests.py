from django.test import TestCase
from .models import Scrim


class ScrimModelTest(TestCase):
    def test_string_representation(self):
        scrim = Scrim(team_name="TEST TEAM")
        self.assertEqual(str(scrim), scrim.team_name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Scrim._meta.verbose_name_plural), "scrims")
