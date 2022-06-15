#!/usr/bin/env python3

# File: ls/tests.py

from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):   # Note: django.test.TestCase
                             # not unittest.TestCase
    def test_bad_maths(self):
        self.assertEqual(1+1, 3)

