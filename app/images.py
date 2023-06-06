import os 
from PIL import Image
import numpy
import ast

#File management system (we can move this code later)

#Takes a room code
#Creates a folder with room_ROOMCODE as name
def new_dir(rc):
    try:
        os.mkdir(os.path.join("img", rc))
    except:
        print("already exists")

#Takes a 1d array out of JS 
#returns a 2d arrayified thingymabob off of that
def matrify(inp):
    ROWLENGTH = 750
    pixels = []
    ret = []
    for i in range(len(inp)//4):
        pixel = (inp[4*i], inp[4*i+1], inp[4*i+2], inp[4*i+3])
        pixels.append(pixel)
    for i in range(len(pixels)//ROWLENGTH):
        row = []
        for j in range(ROWLENGTH):
            row.append(pixels[i*ROWLENGTH+j])
        ret.append(row)
    return ret

def matrifyFromString(inp):
    inp = ast.literal_eval(inp)
    ROWLENGTH = 750
    pixels = []
    ret = []
    for i in range(len(inp)//4):
        pixel = (inp[4*i], inp[4*i+1], inp[4*i+2], inp[4*i+3])
        pixels.append(pixel)
    for i in range(len(pixels)//ROWLENGTH):
        row = []
        for j in range(ROWLENGTH):
            row.append(pixels[i*ROWLENGTH+j])
        ret.append(row)
    return ret


#Takes a room code, array-ified image, and turn count (PLACEHOLDER NAME)
#Creates a standard version of array-ified image and inserts it into the corresponding folder for the specified room code
def insert_img(rc, img, tc):
    Image.fromarray(numpy.array(img).astype(numpy.uint8), mode="RGBA").save(os.path.join("img", rc, tc + ".png"))


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
'''
test4 = [
[(255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122)],
[(255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122)],
[(255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122)],
[(255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122)],
[(255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122), (255, 3, 122)]
]
insert_img("boo", test4, "4")
'''
eximg0 = Image.open('img/test8.png')
test5 = numpy.asarray(eximg0.convert(mode="RGBA"))
insert_img("boo", test5, "5")

eximg1 = Image.open('img/test7.png')
test6 = numpy.asarray(eximg1.convert(mode="RGBA"))
print(test6)
insert_img("boo", test6, "6")

with open("img/test.txt", "r") as file:
    ex = file.read().strip()
raw = matrifyFromString(ex)
print(raw)
#test7 = numpy.asarray([raw])
insert_img("boo", raw, "7")