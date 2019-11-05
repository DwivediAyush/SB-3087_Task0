import cv2
import numpy as np
import os
import csv

def partA():
    s = "C:/Users/HARSH/Documents/E_yantra/SB#3087_Task0/Task0.2/Image Processing/Images/bird.jpg"
    img1 = cv2.imread(s)
    l = []
    # for img1 i.e. bird.jpg
    m = []
    m.append(os.path.basename(s))
    dimensions = img1.shape
    height = dimensions[0]
    width = dimensions[1]
    channels = dimensions[2]
    m.append(height)
    m.append(width)
    m.append(channels)
    x = img1[height // 2, width // 2]
    for i in x:
        m.append(i)
    l.append(m)
    img1 = None

    # for img2 i.e. cat.jpg
    s1 = "C:/Users/HARSH/Documents/E_yantra/SB#3087_Task0/Task0.2/Image Processing/Images/cat.jpg"
    img2 = cv2.imread(s1)
    m = []
    m.append(os.path.basename(s1))
    dimensions = img2.shape
    height = dimensions[0]
    width = dimensions[1]
    channels = dimensions[2]
    m.append(height)
    m.append(width)
    m.append(channels)
    x = img2[height // 2, width // 2]
    for i in x:
        m.append(i)
    l.append(m)
    img2 = None

    # for img3 i.e. flowers.jpg
    s2 = "C:/Users/HARSH/Documents/E_yantra/SB#3087_Task0/Task0.2/Image Processing/Images/flowers.jpg"
    img3 = cv2.imread(s2)
    m = []
    m.append(os.path.basename(s2))
    dimensions = img3.shape
    height = dimensions[0]
    width = dimensions[1]
    channels = dimensions[2]
    m.append(height)
    m.append(width)
    m.append(channels)
    x = img3[height // 2, width // 2]
    for i in x:
        m.append(i)
    l.append(m)
    img3 = None

    # for img4 i.e. horse.jpg
    s3 = "C:/Users/HARSH/Documents/E_yantra/SB#3087_Task0/Task0.2/Image Processing/Images/horse.jpg"
    img4 = cv2.imread(s3)
    m = []
    m.append(os.path.basename(s3))
    dimensions = img4.shape
    height = dimensions[0]
    width = dimensions[1]
    channels = dimensions[2]
    m.append(height)
    m.append(width)
    m.append(channels)
    x = img4[height // 2, width // 2]
    for i in x:
        m.append(i)
    l.append(m)
    with open("C:/Users/HARSH/Documents/E_yantra/SB#3087_Task0/Task0.2/Image Processing/Generated/stats.csv",
              "w") as csvFlie:
        wrt = csv.writer(csvFlie)
        wrt.writerows(l)

def partB():
    

    img=cv2.imread("cat.jpg")
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imshow("img",img[:,:,2])
    cv2.imwrite('cat_red.jpg',img[:, :, 2])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def partC():
    img2=cv2.imread("flowers.jpg")
    cv2.imshow('ima',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    bgra = cv2.cvtColor(img2, cv2.COLOR_BGR2BGRA)

    bgra[...,3] = 0.5
    #print(cv2.split(bgra))
    cv2.imshow('ima',bgra)
    cv2.imwrite('flowers_alpha.png',bgra)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def partD():
    pass

partA()
partB()
partC()
partD()
