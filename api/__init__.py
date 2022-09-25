from config import *
from .items import Item, ItemList


# API configurations
api_bp = Blueprint("api", __name__)
api = Api(api_bp, prefix="/api/v1")

api.add_resource(ItemList, "/news")
api.add_resource(Item, "/news/<uid>")
