import os
from utils.utils import get_source_root, get_project_root

SOURCE_DIR = get_source_root()
PROJECT_ROOT = get_project_root()
HISTORY_LOG_DIR = os.path.join(PROJECT_ROOT, 'pycnc_history.log')
# CONFIG_PATH = os.path.join(ROOT_DIR, 'configuration.conf')