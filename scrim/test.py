from django.test import TestCase
from django.core.urlresolvers import reverse
from django_webtest import WebTest

from .forms import ScrimForm
from .models import Scrim


class ScrimModelTest(TestCase):
    def test_string_representation(self):
        scrim = Scrim(team_name="TEST TEAM")
        self.assertEqual(str(scrim), scrim.team_name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Scrim._meta.verbose_name_plural), "scrims")

    def test_get_absolute_url(self):
        scrim = Scrim.objects.create(team_name='TSM', team_captain='Bjergsen', region='na')
        self.assertIsNotNone(scrim.get_absolute_url())


class ScrimPageTest(TestCase):
    def test_status_code(self):
        response = self.client.get('/scrim/')
        self.assertEqual(response.status_code, 200)

    def test_uses_base_template(self):
        response = self.client.get(reverse('scrim'))
        self.assertTemplateUsed(response, 'base.html')

    def test_uses_scrim_template(self):
        response = self.client.get(reverse('scrim'))
        self.assertTemplateUsed(response, 'scrim/scrim.html')

    def test_one_scrim(self):
        Scrim.objects.create(team_name='Curse', team_captain='Myself', region='na')
        response = self.client.get(reverse('scrim'))
        self.assertContains(response, 'Curse')

    def test_two_scrims(self):
        Scrim.objects.create(team_name='Curse', team_captain='Myself', region='na')
        Scrim.objects.create(team_name='TSM', team_captain='Bjergsen', region='euw')
        response = self.client.get(reverse('scrim'))
        self.assertContains(response, 'Curse')
        self.assertContains(response, 'TSM')


class ScrimDetailTest(TestCase):
    def setUp(self):
        self.scrim = Scrim.objects.create(team_name='TSM', team_captain='Bjergsen', region='na')

    def test_status_code(self):
        response = self.client.get(self.scrim.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_uses_scrim_detail_template(self):
        response = self.client.get(self.scrim.get_absolute_url())
        self.assertTemplateUsed(response, 'scrim/detail.html')

    def test_uses_base_template(self):
        response = self.client.get(self.scrim.get_absolute_url())
        self.assertTemplateUsed(response, 'base.html')

    def test_team_name_in_scrim_detail(self):
        response = self.client.get(self.scrim.get_absolute_url())
        self.assertContains(response, self.scrim.team_name)

    def test_team_captain_in_scrim_detail(self):
        response = self.client.get(self.scrim.get_absolute_url())
        self.assertContains(response, self.scrim.team_captain)


class ScrimFormTest(WebTest):
    def test_valid_data(self):
        form = ScrimForm({
            'team_name': 'Liquid',
            'team_captain': 'Jake',
            'region': 'na',
        })
        self.assertTrue(form.is_valid())
        scrim = form.save()
        self.assertEqual(scrim.team_name, 'Liquid')
        self.assertEqual(scrim.team_captain, 'Jake')
        self.assertEqual(scrim.region, 'na')

    def test_blank_data(self):
        form = ScrimForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'team_name': ['This field is required.'],
            'team_captain': ['This field is required.'],
            'region': ['This field is required.'],
        })
