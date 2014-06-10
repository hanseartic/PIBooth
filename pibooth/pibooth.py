#!/usr/bin/env python3
"""This controlls your raspberry pi-baed photobooth.

You need a DSL-camera connected via USB and some soldering skills, to
use the complete feature-set.
"""

import hardware_controller

class PIBooth:

    def __init__(self):
        hardware_controller.start()

