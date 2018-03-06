# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import sys
import os
from PIL import Image

PATH = os.path.dirname( os.path.abspath(__file__) )
TexturesFile = "textures"
images = []

def get_textures(file):
    for f in os.listdir(file):
        images.append( Image.open( os.path.join(PATH, f) ) )

if __name__ == '__main__':
    print(PATH)