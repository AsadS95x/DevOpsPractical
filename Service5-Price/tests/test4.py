from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import pytest
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_get_price(self):
           response = self.client.get(url_for('price'), json={"Location": "Mayfair", "Size": "5"})
           self.assertEqual(response.status_code, 200)
           self.assertIn(b'3000000', response.data)

