import cv2
import numpy as np
import concurrent.futures
from threading import Thread
import queue
import time

img = cv2.imread('image/image.png', cv2.IMREAD_COLOR)           # rgb

def encode(args):
    i = args[0]
    row = args[1]
    col = args[2]
    # print(i,row,col)
    bytee = bytearray(i, "utf8")
    b = bytee[0]
    b1 = b
    # print(bin(b))
    blue = img[row,col][0]
    green = img[row,col][1]
    red = img[row,col][2]

    blue_c = b & 0b0000111
    # blue = bin(blue)
    blue = blue >> 3
    blue = blue << 3
    blue = blue | blue_c
    # print(bin(blue))

    b = b >> 3
    green_c = b & 0b0000011
    # blue = bin(blue)
    green = green >> 2
    green = green << 2
    green = green | green_c
    # print(bin(green))

    b = b >> 2
    red_c = b & 0b0000011
    # blue = bin(blue)
    red = red >> 2
    red = red << 2
    red = red | red_c
    # print(bin(red))


    img[row,col][0] = blue
    img[row,col][1] = green
    img[row,col][2] = red
    # return None

# def access_row(row,this_string):
#     print(row, this_string," ")
#     col = 0
#     print("string : " + this_string)
#     for i in this_string:
#         encode([i,row,col])

# img[45, 90] = [121, 0, 0]

str1 = input("enter message: ")
# with open('message.txt', 'r', encoding="utf8") as file:
#     temp = file.read()
#     str1 = temp.replace('\n', ' ')
# if len(str1) > (len(img[0]) * len(img)):
#     print("error")
#     quit()
str1 = str(len(str1)) + "," +str1
# access_row(0,str(len(str1))+'@') 
# print(len(str1),len(img)*len(img[0]))
row = 0
# row_length = len(img[0])
# print("length of row is:", row_length)
col = 0
que = queue.Queue()
threads_list = list()


for i in str1:
    if row == len(img[0,col]):
        row = 0
        col +=1
    # encode([i,row,col])
    # print(i)
    t = Thread(target=lambda q, arg1: q.put(encode(arg1)), args=(que, [i,row,col]))
    # t = Thread(target=encode,args=([i,row,col],))
    # if len(str1)> row_length:
    #     str2 = str1[0:row_length-1]
    #     str1 = str1[row_length:-1]
    # else:
    #     str2 = str1
    # t = Thread(target=access_row,args=(row,str2,))
    t.start()
    threads_list.append(t)

    # if len(str1)< row_length:
    #     break

    row += 1


for t in threads_list:
    t.join()
# print( img[0, 0] )
# while not que.empty():
#     result = que.get()
#     print (result)

# print(img[45, 90][0])
# print(len(img))

cv2.imwrite('image/image1.png',img)