from config import *
from utils import *


class ItemList(Resource):

    def get(self):
        "Get Db Items"
        req = client["hackernews_db"]["news"]
        data = [r for r in req.find({})]
        for item in data:
            del item['_id']
        return {
            "message": "Fetch succesfull!",
            "data": data
        }

    def post(self):
        payload = request.get_json()
        return f"You are not allowed to create users through the API", 500


class Item(Resource):

    def get(self, uid: int):
        "Get Item ID Data & Update Db"
        req = client["hackernews_db"]["news"]
        item = requests.get(
            f"https://hacker-news.firebaseio.com/v0/item/{uid}.json")

        # Check and create/update item doc in Db
        db_item = req.find_one({"uid": uid})

        if db_item != None:
            # Update
            req.update_one({
                "uid": uid
            }, {
                "$set": itemData
            })

        else:
            # Create
            del item["id"]
            item["uid"] = uid

            # fetch item

            req.insert_one(itemData)

    def post(self, uid: int):
        "Write new items to News DB"
        payload = request.get_json()

        # get lastest data uid + 1 for new item

        pass
