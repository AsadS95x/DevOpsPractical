from flask_testing import TestCase
from flask import url_for
import requests_mock
from application import app


class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):

        with requests_mock.Mocker() as m:
            m.get('http://housesize:5000/get_size', text='5')
            m.get('http://houselocation:5000/get_location', text='Beverly Hills')
            m.post('http://houseprice:5000/get_price', text='325000')
            response = self.client.get(url_for('home'))
            print (response)
            self.assert200(response)
            self.assertIn("Beverly Hills: with 5 bedrooms, would cost around £325000", response.data.decode())