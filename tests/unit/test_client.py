import unittest

from tests.unit import client


class TestInsertClientInput(unittest.TestCase):
    def setUp(self):
        self.client_input = {
                    "collection": "test",
                    "gender": "female",
                    "name": {
                        "title": "mrs",
                        "first": "ione",
                        "last": "da costa"
                    },
                    "location": {
                        "street": "8614 avenida vinícius de morais",
                        "city": "ponta grossa",
                        "state": "rondônia",
                        "postcode": 97701,
                        "coordinates": {
                            "latitude": "-76.3253",
                            "longitude": "137.9437"
                        },
                        "timezone": {
                            "offset": "-1:00",
                            "description": "Azores, Cape Verde Islands"
                        }
                    },
                    "email": "ione.dacosta@example.com",
                    "dob": {
                        "date": "1968-01-24T18:03:23Z",
                        "age": 50
                    },
                    "registered": {
                        "date": "2004-01-23T23:54:33Z",
                        "age": 14
                    },
                    "phone": "(01) 5415-5648",
                    "cell": "(10) 8264-5550",
                    "picture": {
                        "large": "https://randomuser.me/api/portraits/women/46.jpg",
                        "medium": "https://randomuser.me/api/portraits/med/women/46.jpg",
                        "thumbnail": "https://randomuser.me/api/portraits/thumb/women/46.jpg"
                        }
            }
        self.response_insert = client.post("/v1/client/insert", json=self.client_input)
        self.client_id = self.response_insert.json().get("result")[0]
        self.client_collection = self.client_input["collection"]
        self.response_get_client = client.get(f"/v1/client/{self.client_collection}/{self.client_id}")

    def test_client_input_insert(self):
        self.assertEqual(self.response_insert.status_code, 201)
        self.assertIn("result", self.response_insert.json())
        self.assertIs(type(self.response_insert.json().get("result")), list)

    def test_client_input_get_by_id(self):
        self.assertEqual(self.response_get_client.status_code, 200)
        self.assertIn("result", self.response_get_client.json())
        self.assertIs(type(self.response_get_client.json().get("result")), dict)

    def tearDown(self):
        self.response_delete = client.delete(f"/v1/client/{self.client_collection}")
        self.assertEqual(self.response_delete.status_code, 200)
        self.assertEqual(self.response_delete.json()["result"], True)


class TestClientOutput(unittest.TestCase):
    def setUp(self):
        self.client_output = {
            "collection": "test",
            "client_type": "a",
            "gender": "m",
            "name": {
                "title": "mr",
                "first": "quirilo",
                "last": "nascimento"
            },
            "location": {
                "region": "sul",
                "street": "680 rua treze ",
                "city": "varginha",
                "state": "paraná",
                "postcode": 37260,
                "coordinates": {
                    "latitude": "-46.9519",
                    "longitude": "-57.4496"
                },
                "timezone": {
                    "offset": "+8:00",
                    "description": "Beijing, Perth, Singapore, Hong Kong"
                }
            },
            "email": "quirilo.nascimento@example.com",
            "birthday": "1979-01-22T03:35:31Z",
            "registered": "2005-07-01T13:52:48Z",
            "telephone_numbers": [
                "+556629637520"
            ],
            "mobile_numbers": [
                "+553270684089"
            ],
            "picture": {
                "large": "https://randomuser.me/api/portraits/men/83.jpg",
                "medium": "https://randomuser.me/api/portraits/med/men/83.jpg",
                "thumbnail": "https://randomuser.me/api/portraits/thumb/men/83.jpg"
            },
            "nationality": "BR",
            "object_id_input": "33333333333"
        }
        self.response_insert = [client.post("/v1/client/insert", json=self.client_output) for _ in range(15)]
        self.client_collection = self.client_output["collection"]
        self.client_type = self.client_output["client_type"]
        self.client_region = self.client_output["location"]["region"]
        # self.response_get_by_type_and_region = client.get(f"/v1/client/{self.client_collection}/{self.client_type}/{self.client_region}") # noqa

    def test_client_output_insert(self):
        self.assertTrue(all(filter(lambda x: x == 201, [response.status_code for response in self.response_insert])))
        self.assertTrue(all(filter(lambda x: x == "result", [response.json() for response in self.response_insert])))
        self.assertTrue(all(filter(lambda x: issubclass(list, type(x)), [response.json() for response in self.response_insert]))) # noqa

#     def test_client_output_get_by_type_and_region(self):
#         self.assertEqual(self.response_get_by_type_and_region.status_code, 200)
#         self.assertIn("result", self.response_get_by_type_and_region.json())
#         self.assertIs(type(self.response_get_by_type_and_region.json().get("result")), dict)

    def tearDown(self):
        self.response_delete = client.delete(f"/v1/client/{self.client_collection}")
        self.assertEqual(self.response_delete.status_code, 200)
        self.assertEqual(self.response_delete.json()["result"], True)


if __name__ == "__main__":
    unittest.main()
