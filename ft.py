#!/usr/bin/env python3

# File: ft.py (functional_tests.py)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By

"""
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')

The attributes available for the By class are used to locate elements on a page. These are the attributes available for By class:

ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"  # ****
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

Django's TestCase creates a special test database.
Here we use pypi's unittest.TestCase so need to create one
in settings.py.

"""

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):  # doesn't run if setUp => an exception!!
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has hear about a cool new online to-do app. She goes
        # to checkout its home page
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
                )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1. Buy peacock feathers')
        # now the following are no longer needed...
#       table = self.browser.find_element('id', 'id_list_table')
#       rows = table.find_elements('tag name', 'tr')
#       self.assertIn('1. Buy peacock feathers',
#               [row.text for row in rows])

        # There is still a text box inviting her to add another item.  She
        # enters "Use peacock feathers to make a fly" (Edith if very
        # methodical)
        inputbox = self.browser.find_element('id', 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1. Buy peacock feathers')
        self.check_for_row_in_list_table(
                '2. Use peacock feathers to make a fly')
#       table = self.browser.find_element('id', 'id_list_table')
#       rows = table.find_elements('tag name', 'tr')
#       self.assertIn(
#           '2. Use peacock feathers to make a fly',
#           [row.text for row in rows]
#           )

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to thet effect.
        self.fail('Finish the test!')

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == "__main__":
#   unittest.main(warnings='ignore')
    unittest.main()

