import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer();
path = 'dataset';

def getImagesWithIds(path):
    imagesPath = [os.path.join(path, f) for f in os.listdir(path)]
    print(imagesPath);

getImagesWithIds(path);
