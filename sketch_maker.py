import cv2


## Overview:
## This is a simple code to convert an image to a sketch using opencv

# To read an image
def read_img(filename):
    img = cv2.imread(filename)
    return img


# Inverting (converting to negative)
def inverting(img):
    invert = 255 - img
    return invert


# Making an image grayscale
def gray_scale(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray


# Resizing image according to the length and width specified.
def resize(img, length, width):
    img = cv2.resize(img, (length, width))
    return img


# For color dodging (lighten the image and getting a sketch)
def blending(gray, blur, canvas):
    img_blend = cv2.divide(gray, 255 - blur, scale=256)
    final = cv2.multiply(img_blend, canvas, scale=1 / 256)
    return final


# Applying gaussing blurring according to the kernel specified. (Smoothing of image)
def gaus_blurring(invert):
    blur = cv2.GaussianBlur(invert, ksize=(21, 21), sigmaX=0, sigmaY=0)
    return blur


if __name__ == '__main__':
    file = 'shivek.jpg'
    canvas = 'bg.jpg'
    img = read_img(file)
    canvas = cv2.imread(canvas, cv2.CV_8UC1)
    img = resize(img, 500, 500)
    canvas = resize(canvas, 500, 500)
    gray = gray_scale(img)
    invert = inverting(gray)
    blur = gaus_blurring(invert)
    final = blending(gray, blur, canvas)
    cv2.imshow('img', final)
    cv2.waitKey(0)
