from flask_testing import TestCase
from flask import url_for
from requests_mock import mock
from service_1.application import app


class TestBase(TestCase):

    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):

        with mock() as m:
            m.get('http://housesize:5000/get_size', text=5)
            m.get('http://houselocation:5000/get_location', text='Beverly Hills')
            m.post('http://houseprice:5000/get_price', text=325000)

            response = self.client.get(url_for('index'))


        self.assert200(response)
        self.assertIn("Beverly Hills: with 5 bedrooms, would cost around £325000", response.data.decode())   house_location = requests.get('http://houselocation:5000/get_location').text
