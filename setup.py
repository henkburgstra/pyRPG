
from distutils.core import setup
import py2exe
import os

base_dir = os.path.dirname(__file__)

setup(console=[os.path.join(base_dir, 'game.py')])
