from django.test import TestCase
from django.core.urlresolvers import reverse


class TestHomePage(TestCase):
    def test_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_uses_index_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "lol/index.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "base.html")


class TestLoginPage(TestCase):
    def test_status_code(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_uses_login_template(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "lol/login.html")

    def test_uses_base_template(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "base.html")
