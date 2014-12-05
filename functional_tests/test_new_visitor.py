from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


JASONS_CHROMEDRIVER_PATH = "/home/jason/apps/chromewebdriver/chromedriver"


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):  #
        #self.use_firefox()
        self.use_chrome()  # use firefox. Better error messages.
        self.browser.implicitly_wait(3)

    def tearDown(self):  #
        self.browser.quit()

    def use_firefox(self):
        self.browser = webdriver.Firefox()

    def use_chrome(self):
        self.browser = webdriver.Chrome(
            executable_path=JASONS_CHROMEDRIVER_PATH
        )

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):  #
        """
        Story:
        0. Edith has heard about a cool new online to-do app. She goes
        to check out its homepage

        1. She notices the page title and header mention to-do lists
        2. She is invited to enter a to-do item straight away
        3. She types "Buy peacock feathers" into a text box (Edith's hobby
        is tying fly-fishing lures)
        4. When she hits enter, the page updates, and now the page lists
        "1: Buy peacock feathers" as an item in a to-do list table
        5. There is still a text box inviting her to add another item. She
        enters "Use peacock feathers to make a fly" (Edith is very
        methodical)
        6. The page updates again, and now shows both items on her list


        """

        #[0]
        #self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)

        #[1]
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #[2]
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item'
                         )

        #[3]
        inputbox.send_keys('Buy peacock feathers')
        # When she hits enter, she is taken to a new URL,
        # and now the page lists "1: Buy peacock feathers" as an item in a
        # to-do list table

        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegexpMatches(edith_list_url, '/lists/.+')

        #inputbox = self.browser.find_element_by_id('id_new_item')
        #inputbox.send_keys('Use peacock feathers to make a fly')
        #inputbox.send_keys(Keys.ENTER)

        #[4]
        self.check_for_row_in_list_table(
            '1: Buy peacock feathers'
        )

        self.check_for_row_in_list_table(
            '2: Use peacock feathers to make a fly'
        )

        #[5]
        self.fail("Finish the test!")  #

if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    unittest.main()
