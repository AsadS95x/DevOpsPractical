from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import random
import pytest
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):

    def test_get_size(self):
       with patch('random.randrange') as r:
           r.return_value = 5
           #house_size=5
           response = self.client.get(url_for('size'))
           self.assertEqual(response.status_code, 200)
           self.assertIn(b'5', response.data)