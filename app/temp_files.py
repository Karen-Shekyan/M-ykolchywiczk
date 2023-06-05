import os 
from PIL import Image
import numpy

#File management system (we can move this code later)

#Takes a room code
#Creates a folder with room_ROOMCODE as name
def new_dir(rc):
    os.mkdir(os.path.join("img", rc))

#Takes a room code, array-ified image, and turn count (PLACEHOLDER NAME)
#Creates a standard version of array-ified image and inserts it into the corresponding folder for the specified room code
def insert_img(rc, img, tc):
    Image.fromarray(numpy.array(img).astype(numpy.uint8), mode="RGB").save(os.path.join("img", rc, tc + ".jpg"))


new_dir("boo")
'''
test0 = [
    [0., 0., 0., 200., 200.],
    [0., 0., 0., 200., 200.],
    [0., 0., 0., 200., 200.],
    [0., 0., 0., 200., 200.],
    [0., 0., 0., 200., 255.]
]
print(numpy.array(test0))

insert_img("boo", test0, "0")

test1 = numpy.zeros((10, 10))
print(test1)
insert_img("boo", test1, "1")

test2 = [
    [200., 200., 200., 200., 200.,],
    [200., 200., 200., 200., 200.,],
    [200., 200., 200., 200., 200.,],
    [200., 200., 200., 200., 200.,],
    [200., 200., 200., 200., 200.,]
]
insert_img("boo", test2, "2")

test3 = [
[255, 255, 255, 255, 255],
[255, 255, 255, 255, 255],
[255, 255, 255, 255, 255],
[255, 255, 255, 255, 255],
[255, 255, 255, 255, 255]
]
insert_img("boo", test3, "3")
'''

test4 = [
[(255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122)],
[(255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122)],
[(255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122)],
[(255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122)],
[(255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122)]
]
insert_img("boo", test4, "4")

eximg0 = Image.open('img/test16.jpg')
test5 = numpy.asarray(eximg0)
insert_img("boo", test5, "5")

eximg1 = Image.open('img/test0.jpg')
test6 = numpy.asarray(eximg1)
insert_img("boo", test6, "6")