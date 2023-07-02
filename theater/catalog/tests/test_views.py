from django.test import TestCase
from django.urls import reverse
from catalog.models import Actor
from django.core.paginator import Paginator

class ActorListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 10 authors for pagination tests
        number_of_actors = 10
        for actor_id in range(1, number_of_actors + 1):
            Actor.objects.create(
                name=f'Actor {actor_id}',
                surname=f'Surname {actor_id}',
                date_of_birth='2000-01-01',
                contact='123456789'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/actors/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('actors'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('actors'))
        self.assertTemplateUsed(response, 'catalog/actor_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('actors'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['actor_list']) == 5)

    def test_lists_all_actors(self):
        # 1 страница актеров
        response = self.client.get(reverse('actors') + '?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['actor_list']) == 5)

        # 2 страница актеров
        response = self.client.get(reverse('actors') + '?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['actor_list']) == 5)
