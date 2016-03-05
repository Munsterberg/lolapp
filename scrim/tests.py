from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Scrim


class ScrimModelTest(TestCase):
    def test_string_representation(self):
        scrim = Scrim(team_name="TEST TEAM")
        self.assertEqual(str(scrim), scrim.team_name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Scrim._meta.verbose_name_plural), "scrims")

class TestScrimPage(TestCase):
    def test_status_code(self):
        response = self.client.get('/scrim/')
        self.assertEqual(response.status_code, 200)

    def test_uses_base_template(self):
        response = self.client.get(reverse('scrim'))
        self.assertTemplateUsed(response, 'base.html')

    def test_uses_scrim_template(self):
        response = self.client.get(reverse('scrim'))
        self.assertTemplateUsed(response, 'scrim/scrim.html')
