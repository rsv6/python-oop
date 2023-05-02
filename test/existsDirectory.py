import os
from os import getcwd
from pathlib import Path
import sys
from os.path import exists, dirname, abspath

# Check if exist diratory:
print(os.path.exists('folder'))

# check if exist path absolutely:
print(os.path.exists('folder/file.py'))

# Return current path:
print(os.getcwd())
