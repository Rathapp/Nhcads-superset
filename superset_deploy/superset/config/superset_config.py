from superset.config import * 

SECRET_KEY = "flOZv9DVD3AZ-XyGPClEjvDiYfm6Pigiy6DTrTWsuLx0hJk6xxzp4aB36J5l8GC0l2DgjFZyG2M2Se_HJdFFXg"
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://superset:superset@postgres:5432/superset'
RESULTS_BACKEND = RedisCache(host='redis', port=6379, key_prefix='superset_results') 


APP_NAME = "NCHADS"
APP_ICON = "/static/assets/images/logo.png"
APP_ICON_WIDTH = 20
FAVICONS = [{"href": "/static/assets/images/logo.png"}]

DISPLAY_MAX_ROW = 100000000
RATELIMIT_STORAGE_URL = 'redis://redis:6379/0'

# APP_INITIALIZER = {
#     "CUSTOM_CSS": """
#                     @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Khmer&display=swap');
#                     body, .header, .title, .ant-typography, .chart-label {
#                         font-family: 'Noto Sans Khmer', sans-serif !important;
#                     }
#                     """
# }

FEATURE_FLAGS = {
    "ENABLE_TEMPLATE_PROCESSING": True,
    "ENABLE_REACT_CRUD_VIEWS": True,
    "ENABLE_REACT_USER_GROUPS": True,
}

# Flask-Caching Config
CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_URL': 'redis://redis:6379/0'
}

RESULTS_BACKEND = CACHE_CONFIG


ENABLE_CORS = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Lax"

# Optional: Set allowed origins, etc.
ENABLE_PROXY_FIX = True

