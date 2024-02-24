from typing import Tuple

import os
import numpy as np
import cv2

class Image():
    def __init__(self, raw_image_path: str):
        self.name = os.path.splitext(os.path.basename(raw_image_path))[0]
        self.image = cv2.imread(os.path.abspath(raw_image_path), 1)

   
    def _crop(self, x1: int, y1: int, x2: int, y2: int):
        # Raise error, cannot have image of 0 width or height
        if x1 == x2 or y1 == y2:
            raise ValueError('%s-coordinates cannot be equivalent' % 'x' if x1 == x2 else 'y')
        
        # Flip such that x1 < x2 and y1 < y2
        if x1 > x2:
            x1,x2 = x2,x1
        if y1 > y2:
            y1,y2 = y2,y1

        # Crop the image
        return self.image[y1:y2, x1:x2]
    

    def imshow(self):
        # self._crop(self.images[index], 10, 10, 80,80)
        cropped = self._crop(10, 10, 80,80)
        cv2.imshow('Image', cropped)
        cv2.waitKey(0)

        # cv2.imshow(f'Image {index}', self.images[index])
        # cv2.waitKey(0)


class partsImage(Image):
    pass
    # def crop(self,coords):
    #     print(self.images)


class listImage(Image):
    pass
    # def crop(self,coords):
        # print(self.images)


# partsImages('hello').crop('hu')