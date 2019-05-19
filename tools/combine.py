import cv2
import numpy as np
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file",help="file with paths")

args = parser.parse_args()

f = open(args.file,"r")

scenes = f.readlines()

for i,scene in enumerate(scenes):
    scene = scene.strip()
    img = np.zeros((256,512,3),np.uint8)
    if (scene.find("input") != -1):
#        base = "/vulcan/scratch/jushen/train_generated/" + scene[0:scene.index("input")]
        base =  "train_data_3/"+scene[0:scene.index("input")]
        print(base)
        tr = str(base+"truth.png")
        #img[:,0:256,:] = cv2.imread(tr)
        img[:,0:256,:] = cv2.imread(tr)
        img[:,256:512,:] = cv2.imread(str(base + "input.png"))
        cv2.imwrite(base+"combined_2.png",img)
        print(base+"combined.png")

#img = np.zeros((256,512,3),np.uint8)
#img[:,0:256,:] = cv2.imread('book_l0_yax_315deg_l1_yax_180deg_down.pbrt.png')
#img[:,256:512,:] = cv2.imread('book_l0_yax_315deg_l1_yax_180deg_truth.pbrt.png')
#cv2.imwrite('combined.png',img)
#2B_C2_4L_C6_truth.png
