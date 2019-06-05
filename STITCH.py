import os
import cv2
from PIL import Image
 

def loadImages(imgFolder):
    print("loading Images")
    images = [] 
    for (rootDir, dirNames, fileNames) in os.walk(imgFolder):
        for file in fileNames:
            imgPath = os.path.join(imgFolder, file) 
            images.append(cv2.imread(imgPath))
    return images
def stitchImages(imgFolder,outFolder):
    imageList = loadImages(imgFolder)
    print("image loaded")
    print("stitching images")
    stitcher = cv2.Stitcher.create()
    (status, stitchedImg) = stitcher.stitch(imageList)
    if status == 0:
        cv2.imwrite(outFolder, stitchedImg)
        cv2.imshow("Stitched Image", stitchedImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
    	print("Image stitching failed with status",status)



x = input("enter the folder: ")
number_files = len(os.listdir(x))
print("Number of images in folder to stitch: ",number_files)
   





imgFolder = x
outFolder = "out/output.png"
stitchImages(imgFolder,outFolder)
