from django.test import TestCase
from .models import Drapi


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Drapi.objects.create(title="first drapi", body="a body here")

    def test_title_content(self):
        d = Drapi.objects.get(id=1)
        expected_object_name = f"{d.title}"
        self.assertEqual(expected_object_name, "first drapi")

    def test_body_content(self):
        d = Drapi.objects.get(id=1)
        exptected_object_name = f"{d.body}"
        self.assertEqual(exptected_object_name, "a body here")
