learning-goat-django
====================

A special thanks to the author. Excellent work. :)

This tutorial can be found [here](http://chimera.labs.oreilly.com/books/1234000000754/ "The Goods").


#### some notes, snippets, and cool things:

##### $ grep -E "class|def"

In chapter 6 the author uses ```$ grep -E "class|def" lists/tests.py```.  This snippet outputs the equivalent of a printy print of classes and their functions. What an amazing little trick.  Also, awesomely this works for Ruby source files as well. Additionally, using sublime text file search (with regex on and with 'show context' off)  class|def  looks very similar to the terminal output (thanks, [Rick Carlino](https://github.com/rickcarlino) for the extras). Here is the terminal output:

    class ListViewTest(TestCase):
        def test_home_page_displays_all_list_items(self):
    class ItemModelTest(TestCase):
        def test_saving_and_retrieving_items(self):
    class HomePageTest(TestCase):
        def test_root_url_resolves_to_home_page_view(self):
        def test_home_page_returns_correct_html(self):
        def list_item_post_request(self):
        def test_home_page_can_save_a_POST_request(self):
        def test_home_page_redirects_after_POST(self):
        def test_home_page_only_saves_items_when_necessary(self):
        def test_home_page_displays_all_list_items(self):

