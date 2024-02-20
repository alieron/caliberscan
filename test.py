import cv2

from caliberscan import movement

parts_images = [cv2.imread("test/omega625image.png", 0)]
parts_lists = [cv2.imread(path,0) for path in ("test/omega625list1.png", "test/omega625list2.png")]

omega625 = movement.Movement(parts_images, parts_lists)

# print(type(Omega625.parts_images[0]))
cv2.imshow('img', omega625.parts_images[0])
cv2.waitKey(0)