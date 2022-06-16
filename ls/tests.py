#!/usr/bin/env python3

# File: ls/tests.py

from django.urls import resolve
from django.test import TestCase
from ls.views import home_page

# Create your tests here.

smoketest = """
class SmokeTest(TestCase):   # Note: django.test.TestCase
                             # not unittest.TestCase
    def test_bad_maths(self):
        self.assertEqual(1+1, 3)
"""

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  # django.urls.resolve
                            # returns a ResolverMatch object:
                  # metadata of URL incl the view function: found.func
        self.assertEqual(found.func, home_page)
