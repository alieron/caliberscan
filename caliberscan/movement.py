from typing import List

import numpy as np
import cv2

class Movement():
    def __init__(self, parts_images: List[np.ndarray] , parts_lists: List[np.ndarray]):
        self.parts_images = parts_images
        self.parts_lists = parts_lists
    

    # def func():


