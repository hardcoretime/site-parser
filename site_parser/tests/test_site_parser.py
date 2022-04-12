#!/usr/bin/env python3
import os.path
import unittest

from site_parser import is_url, get_urls


class TestSiteParser(unittest.TestCase):

    def setUp(self) -> None:
        self.test_urls = ['https://yandex.ru', 'https://mail.ru', 'https://rutube.ru']

    def test_is_url(self):
        self.assertTrue(is_url(self.test_urls[0]))
        self.assertTrue(is_url(self.test_urls[1]))
        self.assertTrue(is_url(self.test_urls[2]))

    def test_get_url(self):
        with open(f'{os.path.dirname(__file__)}/index.html', 'r') as file:
            test_html_page = file.read()

        urls = get_urls(test_html_page)

        self.assertTrue(self.test_urls == urls)


if __name__ == '__main__':
    unittest.main()
