import unittest
import requests

from ..RejestrKont import RejestrKont

class TestUniqueAccount(unittest.TestCase):
    body1 = {
        "imie": "nick",
        "nazwisko": "cave",
        "pesel": "03804628461"
    }
    body2 = {
        "imie": "john",
        "nazwisko" : "smith",
        "pesel": "03704428531"
    }

    url = "http://localhost:5000"

    def test_1_create_more_accounts(self):
        create_resp1 = requests.post(self.url + "/konta/stworz_konto", json = self.body1)
        self.assertEqual(create_resp1.status_code, 201)
        create_resp2 = requests.post(self.url + "/konta/stworz_konto", json = self.body2)
        self.assertEqual(create_resp2.status_code, 201)
        get_resp = requests.get(self.url + "/konta/ile_kont")
        self.assertEqual(get_resp.status_code, 200)
        res_body = get_resp.json()
        self.assertEqual(res_body, "Ilość kont w rejestrze 2")
    
    def test_2_adding_existing_account(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json = self.body1)
        self.assertEqual(create_resp.status_code, 400)
        get_resp = requests.get(self.url + "/konta/ile_kont")
        self.assertEqual(get_resp.status_code, 200)
        res_body_get = get_resp.json()
        self.assertEqual(res_body_get, "Ilość kont w rejestrze 2")

    def test_cleaning(self):
        requests.delete(self.url + f"/konta/konto/{self.body1['pesel']}", json = self.body1)
        requests.delete(self.url + f"/konta/konto/{self.body2['pesel']}", json = self.body2)
 
    @classmethod
    def tearDownClass(cls):
        RejestrKont.registry = []