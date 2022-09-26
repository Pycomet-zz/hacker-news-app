from api import *
import unittest

# Test Endpoints Data


class TestAPI(unittest.TestCase):
    def test_get_db_news_list(self):
        "Test fetching using the endpoint resource"
        res = requests.get("http://127.0.0.1:8080/api/v1/news").json()
        assert res["code"] == 200
        assert len(res["data"]) > 0

    def test_get_filtered_news_list(self):
        "Test filtering using the endpoint resource"
        res1 = requests.post("http://127.0.0.1:8080/api/v1/news",
                             json={'types': 'job', 'search': 'codefred'}).json()
        res2 = requests.post("http://127.0.0.1:8080/api/v1/news",
                             json={'types': 'job,story', 'search': ''}).json()
        res3 = requests.post("http://127.0.0.1:8080/api/v1/news",
                             json={'types': '', 'search': 'help'}).json()
        assert res1["code"] == 200
        assert res2["code"] == 200
        assert res3["code"] == 200

    def test_get_single_news(self):
        "Fetch a single news object from database"
        res1 = requests.get(
            "http://127.0.0.1:8080/api/v1/news/32953111"
        ).json()  # valid
        res2 = requests.get(
            "http://127.0.0.1:8080/api/v1/news/00053732"
        ).json()  # invalid
        assert res1["code"] == 200
        assert res2["code"] == 404

    def test_post_single_news(self):
        "test creating new uniques news to DB"
        res1 = requests.post(
            "http://127.0.0.1:8080/api/v1/news/32953732",
            json={
                "by": "codefred",
                "type": "job",
                "time": 2436273623,
                "deleted": False,
                "dead": False,
                "text": "This is a test job",
                "url": "https://google.com",
                "title": "Flow design",
            },
        ).json()
        assert res1["code"] == 200


if __name__ == "__main__":
    unittest.main()
