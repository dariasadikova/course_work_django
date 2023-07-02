from django.test import TestCase
from catalog.models import Actor

class ActorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Actor.objects.create(name='Мария', surname='Иванова', date_of_birth='1990-01-21', contact='89853120679')

    def test_name_label(self):
        actor = Actor.objects.get(id=1)
        field_label = actor._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Имя')

    def test_surname_label(self):
        actor = Actor.objects.get(id=1)
        field_label = actor._meta.get_field('surname').verbose_name
        self.assertEqual(field_label, 'Фамилия')

    def test_date_of_birth_label(self):
        actor = Actor.objects.get(id=1)
        field_label = actor._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'Дата рождения')

    def test_contact_label(self):
        actor = Actor.objects.get(id=1)
        field_label = actor._meta.get_field('contact').verbose_name
        self.assertEqual(field_label, 'Номер телефона')

    def test_name_max_length(self):
        actor = Actor.objects.get(id=1)
        max_length = actor._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_surname_max_length(self):
        actor = Actor.objects.get(id=1)
        max_length = actor._meta.get_field('surname').max_length
        self.assertEqual(max_length, 200)


