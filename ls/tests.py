#!/usr/bin/env python3

# File: ls/tests.py

from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from ls.views import home_page
from ls.models import Item

# Create your tests here.

"""
Django's TestCase creates a special test database.
"""

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


    def test_can_save_a_POST_request(self):
        self.client.post('/',
                data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        # redirect status code is 302 

    def test_redirects_after_POST(self):
        response = self.client.post('/',
                data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'],
                '/lists/the-only-list-in-the-world/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get(
                '/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')


    def test_displays_all_items(self):
        # setup
        Item.objects.create(text='itemy 1')
        Item.objects.create(text='itemy 2')
        # exercise
        response = self.client.get('/lists/the-only-list-in-the-world/')
        # assert
        self.assertContains(response, 'itemy 1')
        self.assertContains(response, 'itemy 2')
        # 'assertContains': provided by Django- knows how to deal with
        # responses and the bytes of their content. Therefore no need:
#       self.assertIn('itemy 1', response.content.decode())
#       self.assertIn('itemy 2', response.content.decode())
