from config import *
from models import *


def get_item(uid: int) -> object:
    all_data = client["hackernews_db"]["news"]
    result = all_data.find_one({"uid": uid})
    return result


def check_db_item(uid: int) -> (bool, dict or None):
    "Check whether item exists on Db"
    item = get_item(uid)
    if item == None:
        return False, None
    else:
        return True, item


def create_item(uid: int, data: dict) -> bool:
    "Creates new item into DB"
    all_data = client["hackernews_db"]["news"]

    try:
        if "id" in data.keys():
            del data["id"]
        data["uid"] = uid

        all_data.insert_one(data)
        return True

    except:
        logging.warning("Error in creating a new item data!")
        return False


def update_item(uid: int, data: dict) -> bool:
    "Update an existing item with data"
    all_data = client["hackernews_db"]["news"]
    try:
        item = get_item(uid)
        all_data.update_one({"uid": uid}, {"$set": data})
        return True

    except:
        logging.warning("Error in updating item data!")
        return False


def delete_item(uid: int) -> bool:
    "Deleting a post from Database"
    all_data = client["hackernews_db"]["news"]
    try:
        item = get_item(uid)
        all_data.delete_one({"uid": uid})
        return True

    except:
        logging.warning("Error in deleting item!")
        return False


def get_comment(uid: int):
    "Get single comment"
    comment = requests.get(
        f"https://hacker-news.firebaseio.com/v0/item/{uid}.json"
    ).json()

    if comment["type"] == "comment" and "kids" not in comment.keys():
        return {"uid": uid, "text": comment.get("text")}
    elif comment["type"] == "comment" and "kids" in comment.keys():
        comments = get_comments(comment["kids"])
        return comments
    else:
        logging.warning(f"Error fetching comment - {uid}")
        return {"uid": uid, "text": ""}


def get_comments(uids: [int]) -> []:
    "Swap comment IDs with comments"
    res = []

    for uid in uids:
        comment = get_comment(uid)
        res.append(comment)

    return res


async def sync_HN_to_DB(uid: int):
    "Fetch Data From Hacker News By Type"

    item_response = requests.get(
        f"https://hacker-news.firebaseio.com/v0/item/{uid}.json"
    )

    item = item_response.json()

    # Get comments in order
    if "kids" in item.keys():
        comments = get_comments(item["kids"])
    else:
        comments = []

    del item["id"]
    item["uid"] = uid

    # Sort through Item Types
    if item["type"] == "job":
        job = Job.from_dict(item)
        clean_data = job.to_dict()

    elif item["type"] == "story":
        story = Story.from_dict(item)
        clean_data = story.to_dict()

    elif item["type"] == "poll":
        poll = Poll.from_dict(item)
        clean_data = poll.to_dict()

        # ADD Parts
        parts = []
        if "parts" in item.keys():
            for part in item["parts"]:
                option = get_item(uid=int(part))
                parts.append[option["score"]]

        clean_data["parts"] = parts
    else:
        return False

    # ADD COMMENTS BEFORE SEDNING TO DB
    clean_data["comments"] = comments

    exist, db_item = check_db_item(uid=uid)

    if exist == True and db_item["deleted"] == True:
        status = delete_item(uid=uid)
        logging.warning(f"Item {uid} Deleted - {status}")

    elif exist == True and db_item["deleted"] == False:

        status = update_item(uid=uid, data=clean_data)
        logging.warning(f"Item {uid} Updated - {status}")

    else:

        status = create_item(uid=uid, data=clean_data)
        logging.warning(f"Item {uid} Created - {status}")

    return status
