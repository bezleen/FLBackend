from src.schemas.api import ApiMeta

from .index import bp as rest_index
from .fl import api as FlApi


v1_bp = ApiMeta.blueprint
api = ApiMeta.api

# routing api for app
api.add_namespace(FlApi, path='/fl')

DEFAULT_BLUEPRINTS = [
    v1_bp,
    rest_index
]
