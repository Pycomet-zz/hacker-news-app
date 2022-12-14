from config import *
from utils import *


class ItemList(Resource):
    def get(self):
        "Get Db Items"
        req = client["hackernews_db"]["news"]
        data = [r for r in req.find({})][::-1]
        for item in data:
            if "_id" in item.keys():
                del item["_id"]
            item["time"] = get_datetime(item["time"])

        return {"message": "Fetch Succesfully", "data": data, "code": 200}

    def post(self):
        "Filter end point for retrieving data"
        payload = request.get_json()

        types = payload["types"].split(",")

        search = payload["search"]

        # Extract based on types first
        req = client["hackernews_db"]["news"]
        if len(types) > 0 and types[0] != "":

            raw_data = []
            if search != "":

                for ts in types:
                    [
                        raw_data.append(r)
                        for r in req.find({"$text": {"$search": search}, "type": ts})
                    ]
            else:

                for ts in types:
                    [raw_data.append(r) for r in req.find({"type": ts})]
            data = raw_data[::-1]
        else:
            data = [r for r in req.find({"$text": {"$search": search}})][::-1]

        for item in data:
            if "_id" in item.keys():
                del item["_id"]
            item["time"] = get_datetime(item["time"])

        return {"message": "Fetched Successfully", "data": data, "code": 200}


class Item(Resource):
    def get(self, uid: int):
        "Get Item ID Data & Update Db"
        exist, dbItem = check_db_item(int(uid))

        if exist == True:

            del dbItem["_id"]
            dbItem["time"] = get_datetime(dbItem["time"])

            return {"message": "Item Fetch Success", "data": dbItem, "code": 200}

        else:

            return {
                "message": "Item Does Not Exist In Database",
                "data": None,
                "code": 404,
            }

    def post(self, uid: int):
        "Write new items to News DB"
        payload = request.get_json()

        # fetch latest uid
        latest_uid = requests.get(
            "https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty"
        ).json()

        new_uid = int(latest_uid) + 1

        # Check that it does not exist
        exist, dbItem = check_db_item(uid=new_uid)

        if exist == False:

            status = create_item(uid=new_uid, data=payload)

            if status == True:
                return {"message": "New Item Created", "data": status, "code": 200}
            else:
                return {
                    "message": "New Item Creation Failed",
                    "data": status,
                    "code": 401,
                }

        else:

            return {"message": "Item Already Exist", "data": dbItem, "code": 409}
