import os
from functools import partial

base_path = partial(
    os.path.join, os.path.dirname(os.path.abspath(__file__))
)
ELEGANT_DARK = base_path("ElegantDark.qss")
MANJARO = base_path("ManjaroMix.qss")
MATERIAL = base_path("MaterialDark.qss")
TESTING = base_path("testing.qss")
