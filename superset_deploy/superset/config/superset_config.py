
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

