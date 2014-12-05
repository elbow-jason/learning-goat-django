from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

# Create your tests here.
from lists.views import home_page
from lists.models import Item


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        text1 = 'The first (ever) list item'
        text2 = 'Item the second'

        first_item = Item()
        first_item.text = text1
        first_item.save()

        second_item = Item()
        second_item.text = text2
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, text1)
        self.assertEqual(second_saved_item.text, text2)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def list_item_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'
        return request

    def test_home_page_can_save_a_POST_request(self):
        request = self.list_item_post_request()
        home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_home_page_redirects_after_POST(self):
        request = self.list_item_post_request()
        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_home_page_only_saves_items_when_necessary(self):
        req = HttpRequest()
        home_page(req)
        self.assertEqual(Item.objects.count(), 0)

    def test_home_page_displays_all_list_items(self):
        Item.objects.create(text="itemy 1")
        Item.objects.create(text="itemy 2")

        request = HttpRequest()
        response = home_page(request)

        self.assertIn("itemy 1", response.content.decode())
        self.assertIn("itemy 2", response.content.decode())
