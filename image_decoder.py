from typing import Sized
import cv2
import numpy as np

img = cv2.imread('image/image1.png', cv2.IMREAD_COLOR)           # rgb
# alpha_img = cv2.imread('image/image.png', cv2.IMREAD_UNCHANGED) # rgba
# gray_img = cv2.imread('image/image.png', cv2.IMREAD_GRAYSCALE)  # grayscale

# print (type(img))
# print ('RGB shape: ', img.shape)        # Rows, cols, channels
# print ('ARGB shape:', alpha_img.shape)
# print ('Gray shape:', gray_img.shape)
# print ('img.dtype: ', img.dtype)
# print ('img.size: ', img.size)

# print( img[45, 90] ) #= [200 106   5]       # mostly blue
# print(img[173, 25]) # = [  0 111   0]      # green
# print( img[145, 208])  #=  [  0   0 177]    # red

# img[45, 90] = [0, 0, 0]

# cv2.imwrite('image/image1.png',img)
def decode(row,col):
    b = 0b00000011 &  img[row, col][2]
    # print(bin(img[row, col][2]))
    b = b << 2
    b = b | (0b00000011 &  img[row, col][1])
    # print(bin(img[row, col][1]))
    b = b << 3
    b = b | (0b00000111 &  img[row, col][0])
    a = chr(b)
    return a

row = 0
col = 0
# for i in str1:
#     if row == len(img[0,col]):
#         row = 0
#         col +=1
flag = True
count = ''
my_str = ''
size = 0
while True:
    if row == len(img[0,col]):
        row = 0
        col +=1
    
    a = decode(row,col)
    print(a)
    if flag == True:
        if a != ',':
            count = count + a
        else:
            flag = False
            size = int(count)
    else:
        if size != 0:
            my_str = my_str + a
        else:
            break
        size -= 1
    row += 1
    # print(count,flag , b)
    # print(bin(img[row, col][0]))
    # print(bin(b))
    # print(chr(b))
    # print(img[0,0])

print(my_str)

# from typing import Sized
# import cv2
# import numpy as np

# img = cv2.imread('image/image1.png', cv2.IMREAD_COLOR)           # rgb

# def decode(row,col):
#     # row = args[0]
#     # col = 0
#     # if row == (len(img[0,col])-1):
#     #     row = 0
#     #     col +=1
#     b = 0b00000011 &  img[row, col][2]
#     # print(bin(img[row, col][2]))
#     b = b << 2
#     b = b | (0b00000011 &  img[row, col][1])
#     # print(bin(img[row, col][1]))
#     b = b << 3
#     b = b | (0b00000111 &  img[row, col][0])
#     a = chr(b)
#     return a
# def access_row(row):
#     str1 = ""
#     col = 0
#     while True:
#         a = decode(row,col)
#         print(a)
#         if a == "@" or col == len(img[0])-1:
#             break
#         else:
#             str1 = str1 + a
#         col += 1
#     return str1

# # decode(0)
# # row = 0
# # col = 0
# # flag = True
# # count = ''
# # my_str = ''
# # size = 0
# # while True:
# #     # if row == (len(img[0,col])-1):
# #     #     row = 0
# #     #     col +=1
# #     # b = 0b00000011 &  img[row, col][2]
# #     # # print(bin(img[row, col][2]))
# #     # b = b << 2
# #     # b = b | (0b00000011 &  img[row, col][1])
# #     # # print(bin(img[row, col][1]))
# #     # b = b << 3
# #     # b = b | (0b00000111 &  img[row, col][0])
# #     # a = chr(b)
# #     a = decode([row,col])
# #     if flag == True:
# #         if a != ',':
# #             count = count + a
# #         else:
# #             flag = False
# #             size = int(count)
# #     else:
# #         if size != 0:
# #             my_str = my_str + a
# #         else:
# #             break
# #         size -= 1
# #     row += 1
# #     # print(count,flag , b)
# #     # print(bin(img[row, col][0]))
# #     # print(bin(b))
# #     # print(chr(b))
# #     # print(img[0,0])
# my_str = access_row(0)
# print(my_str)