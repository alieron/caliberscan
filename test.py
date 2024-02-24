import cv2

# from caliberscan import Movement

# parts_images = [cv2.imread("test/omega625image.png", 0)]
# parts_lists = [cv2.imread(path,0) for path in ("test/omega625list1.png", "test/omega625list2.png")]

# omega625 = movement.Movement(parts_images, parts_lists)

# # print(type(Omega625.parts_images[0]))
# cv2.imshow('img', omega625.parts_images[0])
# cv2.waitKey(0)

from caliberscan.movement import Movement

parts_paths = ['test/omega625parts.png']
list_paths = ['test/omega625list1.png', 'test/omega625list2.png']

# print(__file__)

# images.listImages(list_paths).imshow()

omega = Movement('test/', parts_paths, list_paths)

omega.list_images[0].imshow()
# img = cv2.imread('test\omega625list1.png',1)
# cv2.imshow('Image',img)
# cv2.waitKey(0)