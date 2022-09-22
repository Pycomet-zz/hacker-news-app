from config import *


def get_item(uid: int) -> object:
    all_data = client["hackernews_db"]["news"]
    result = all_data.find_one({"_id": ObjectId(uid)})
    return result


def check_db_item(uid: int) -> bool:
    "Check whether item exists on Db"
    item = get_item(uid)
    if item == None:
        return False
    else:
        return True


def update_item(uid: int, data: dict) -> bool:
    "Update an existing item with data"
    try:
        item = get_item(uid)
        item.update_one({"_id": ObjectId(uid)}, {"$set": data})
        return True

    except:
        logging.warning("Error in updating item data!")
        return False


def create_item(data: dict) -> bool:
    "Creates new item into DB"
    all_data = client["hackernews_db"]["news"]

    try:
        print(data)
        data.update({"_id": ObjectId(data["id"])})

        all_data.insert_one(data)
        return True

    except:
        logging.warning("Error in creating a new item data!")
        return False


def sync_HN_to_DB(uid: int, item_type: str):
    "Fetch Data From Hacker News By Type"
    item = requests.get(
        f"https://hacker-news.firebaseio.com/v0/item/{uid}.json")

    if item_type == "job":
        pass

    elif item_type == "story":
        pass

    elif item_type == "comment":
        pass

    elif item_type == "poll":
        pass

    elif item_type == "pollopt":
        pass

    else:
        return False
