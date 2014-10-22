import json
try:
    from unittest import mock
except ImportError:
    import mock

from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory
from django.test import TestCase

from facebook_javascript_authentication import views


class AuthenticateFacebookUserTest(TestCase):
    @mock.patch('facebook_auth.utils.get_from_graph_api')
    def test_if_user_is_authenticated(self, graph_api_mock):
        factory = RequestFactory()
        request = factory.post('/')
        session = SessionMiddleware()
        session.process_request(request)
        request.POST = {
            'access_token': 'aaa',
        }
        data_dict = {'email': 'aaa@aaa.com', 'name': 'Aaa',
                     'last_name': 'Zzz',
                     'id': '740277901',
                     'username': 'aaaa',
                     'link': 'https://www.facebook.com/aaaa',
                     'gender': 'male',
                     'locale': 'pl_PL',
                     'first_name': 'Asss',
                     'verified': True, 'timezone': 2}
        graph_api_mock.return_value = data_dict

        response = views.authenticate(request)
        self.assertEqual(200, response.status_code)
        response_data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data_dict['last_name'], response_data['last_name'])
        self.assertEqual(data_dict['email'], response_data['email'])
        self.assertEqual(data_dict['id'], response_data['username'])
        self.assertEqual(data_dict['first_name'], response_data['first_name'])
        self.assertEqual('ok', response_data['status'])
