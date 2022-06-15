#!/usr/bin/env python3

# File: ft.py (functional_tests.py)

from selenium import webdriver
#import unittest

#from selenium.webdriver.common.keys import Keys
#import time

#class NewVisitorTest(unittest.TestCase):

#    def setUp(self):
#        self.browser = webdriver.Firefox()

#    def tearDown(self):
#        self.browser.quit()

#    def check_for_row_in_list_table(self, row_text):
#        table = self.browser.find_element_by_id('id_list_table')
#        rows = table.find_elements_by_tag_name('tr')
#        self.assertIn(row_text, [row.text for row in rows])
        

#    def test_can_start_a_list_and_retrieve_it_later(self):
#        # Edith goes to check home page of cool app:
#        self.browser.get('http://localhost:8000')
#
#        # She notices title and header mention to-do lists:
#        self.assertIn('To-Do', self.browser.title)
#
#        header_text = self.browser.find_element_by_tag_name('h1').text
#        self.assertIn('To-Do', header_text)

#        # She is invited to enter an item into the to do list:
#        inputbox = self.browser.find_element_by_id('id_new_item')
#        self.assertEqual(inputbox.get_attribute('placeholder'),
#                        'Enter a to-do item')


#        # She enters 'Buy peacock feathers':
#        inputbox.send_keys("Buy peacock feathers")

#        # Upon hitting enter, the page updates showing a list:
#        # "1: Buy peacock feathers" as an item in a to-do list
#        inputbox.send_keys(Keys.ENTER)
#        time.sleep(1)
#        self.check_for_row_in_list_table('1: Buy peacock feathers')
#
#        # There is still a text box inviting her to enter another item
#        # She enters 'Use peacock feathers to make a fly'
#        inputbox = self.browser.find_element_by_id('id_new_item')
#        inputbox.send_keys("Use peacock feathers to make a fly")
#        inputbox.send_keys(Keys.ENTER)
#        time.sleep(1)
#
#        # The page updates again showing both items on her list
#        self.check_for_row_in_list_table(
#                '2: Use peacock feathers to make a fly')
#
#
#        # Will site remember her list? Then she sees a unique URL has
#        # been generated for her with explanatory text to that effect.
#
#        self.fail('Finish the test!')
#
#
#        # She visits that url and sees her list.
#
#        # Satisfied
#
#if __name__ == '__main__':
#    unittest.main(warnings='ignore')

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title

