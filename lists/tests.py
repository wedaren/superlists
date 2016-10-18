from django.test import TestCase
from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # 以下两个，个人觉得都是常量测试，没必要
        # # self.assertTrue(response.content.startswith('b<html>'))
        # # self.assertIn(b'<title>To-Do lists</title>',response.content)
        # # self.assertTrue(response.content.endswith('b</html>'))
        #
        # # expected_html = render_to_string('home.html')
        # # self.assertEqual(response.content.decode(),expected_html)
