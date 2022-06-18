#!/usr/bin/env python3

# File: ls/tests.py

from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from ls.views import home_page
from ls.models import Item

# Create your tests here.

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        """
        See https://docs.djangoproject.com/en/1.11/intro/tutorial01/
        Written in a (not recommended) very verbose style.
        Wait until Chapter 15 for concise version.
        """
        first_item = Item()  # django.db.models.Item
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()  # django.db.models.Item
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
            # database querying API: Item.objects (a class attribute)
            # retrieves all records for table in question
            # in a (list like object called a Query Set
            # from which we can extract individual objects or
            # call further functions like .count()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text,
                'The first (ever) list item')
        self.assertEqual(second_saved_item.text,
                'Item the second')


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  # django.urls.resolve
                            # returns a ResolverMatch object:
                  # metadata of URL incl the view function: found.func
        self.assertEqual(found.func, home_page)

#   def test_home_page_returns_correct_html(self):
    def test_uses_home_template(self):
        # instead of creating an HttpRequest object
        # and calling the view function directly...
#       request = HttpRequest()  # object seen by Django
#                                # when browser asks for a page
#       response = home_page(request)
#       ...use Django testclient...
        response = self.client.get('/')

        old_code = '''
        html = response.content.decode('utf8')
        self.assertTrue(html.strip().startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')
'''

    def test_can_save_a_POST_request(self):
        response = self.client.post('/',
                data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

