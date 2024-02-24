from typing import Tuple

import os
import numpy as np
import cv2

from caliberscan import images

class Movement():
    def __init__(self, working_dir: str, parts_image_paths: Tuple[str, str], list_image_paths: Tuple[str, str]):
        self.working_dir = os.path.abspath(working_dir)
        self.parts_images = [images.partsImage(path) for path in parts_image_paths]
        self.list_images = [images.listImage(path) for path in list_image_paths]

        print(self.working_dir)

    def straighten_parts_images(self, auto: bool = True, crop: bool = True):
        for index, image in enumerate(self.parts_images):
            if auto:
                # Auto document straightener
                pass
            else:
                # Manual point setting
                pass

            if crop:
                result = 0
                # result = image._crop(x1,y1,x2,y2)

            # Overwrite the 
            self.parts_images[index] = result
        
            
            
    

    # def func():


