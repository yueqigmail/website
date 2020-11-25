import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
path1=os.path.abspath('.')
print(path1)
print(BASE_DIR)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'templates'),
]
print(STATICFILES_DIRS)