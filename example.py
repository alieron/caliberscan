import cv2

from calscan import movement, partimager, listparser

Omega625 = movement.Movement([cv2.imread("D:/code/calscan/test/omega625image.png", 0)],
                             [cv2.imread(path,0) for path in ("D:/code/calscan/test/omega625list1.png", "D:/code/calscan/test/omega625list2.png")])

print(type(Omega625.parts_images[0]))
cv2.imshow('img', Omega625.parts_images[0])
cv2.waitKey(0)