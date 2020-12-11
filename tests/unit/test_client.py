import unittest

from tests.unit import client


class TestInsertClientInput(unittest.TestCase):
    json = {
            "collection": "string",
            "gender": "string",
            "name": {},
            "location": {},
            "email": "string",
            "dob": {},
            "registered": {},
            "phone": "string",
            "picture": {}
            }
    response = client.post("/v1/database/insert", json=json)

    def test_http_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_return_key(self):
        self.assertIn("result", self.response.json())

    def test_return_type(self):
        self.assertIs(type(self.response.json().get("result")), list)
