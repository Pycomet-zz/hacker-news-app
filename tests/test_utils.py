from api import *
import unittest


# Unit Tests For The Bot

# Utility Function Tests
from utils import *


class TestUtils(unittest.TestCase):
    # Test CRUD Functions
    def test_create_item(self):
        "testing the create item into database"
        test_data = {
            "by": "codefred",
            "type": "job",
            "time": 2436273623,
            "deleted": False,
            "dead": False,
            "text": "This is a test job",
            "url": "https://google.com",
            "title": "Flow design",
        }
        res = create_item(12345678, test_data)
        assert res == True

    def test_check_item(self):
        "Fetching User From Database"
        res1, _ = check_db_item(32985957)
        res2, _ = check_db_item(00000)
        assert res1 == True
        assert res2 == False

    def test_update_item(self):
        "Test Update Item To DB"
        test_data = {"title": "Flow Design Updated"}
        res = update_item(12345678, test_data)
        assert res == True

    def test_delete_item(self):
        res = delete_item(12345678)
        assert res == True


if __name__ == "__main__":
    unittest.main()
