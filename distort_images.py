import cv2
import numpy as np
from PIL import Image
import os
from random import randint

def _rotate_image(im: np.array, angle: float) -> np.array:
    (h, w) = im.shape[:2]
    center = (w / 2, h / 2)
    
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(im, M, (w, h))
    return rotated

def _horizontally(im: np.array, stretch_factor: int) -> np.array:
    for _ in range(stretch_factor):
        im = np.insert(im, 0, [0, 0, 0], axis=1)
        im = np.insert(im, im.shape[1], [0, 0, 0], axis=1)

    stretched_image = Image.fromarray(im)
    converted_image = stretched_image.resize((32, 32))
    
    return np.array(converted_image)

def _vertically(im: np.array, stretch_factor: int) -> np.array:
    for _ in range(stretch_factor):
        im = np.insert(im, 0, [0, 0, 0], axis=0)
        im = np.insert(im, im.shape[0], [0, 0, 0], axis=0)

    stretched_image = Image.fromarray(im)
    converted_image = stretched_image.resize((32, 32))

    return np.array(converted_image)

def _offset_image(im: np.array, x_offset: int, y_offset: int) -> np.array:
    # Get the image dimensions
    (h, w) = im.shape[:2]

    # Create a blank image with the same dimensions
    blank_image = np.zeros((h, w, 3), dtype=np.uint8)

    # Calculate new dimensions considering the offset
    if y_offset >= 0:
        y_start = y_offset
        y_end = h
    else:
        y_start = 0
        y_end = h + y_offset

    if x_offset >= 0:
        x_start = x_offset
        x_end = w
    else:
        x_start = 0
        x_end = w + x_offset

    # Calculate the corresponding source region in the original image
    src_y_start = max(-y_offset, 0)
    src_y_end = min(h - y_offset, h)
    src_x_start = max(-x_offset, 0)
    src_x_end = min(w - x_offset, w)

    # Place the original image onto the blank image with the offset
    blank_image[y_start:y_end, x_start:x_end] = im[src_y_start:src_y_end, src_x_start:src_x_end]

    return blank_image

def distortion_run(iterations: int, input_path: str, output_path:str) -> None:
    
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
     
    files = os.listdir(input_path)
    
    for file in files:
        path_to_file = os.path.join(input_path, file)
        
        output_dir_name = file.split(".")[0]
        
        output_path_file = os.path.join(output_path, output_dir_name)

        if not os.path.isdir(output_path_file):
            os.mkdir(os.path.join(output_path_file))
            
        im = cv2.imread(path_to_file)

        for i in range(iterations):
            stretch_factor_h = randint(0,15)
            stretch_factor_w = randint(0, 15)
            offset_x = randint(-5, 5)
            offset_y = randint(-3, 3)
            angle = randint(-30, 30)
            
            img = _offset_image(im, offset_x, offset_y)
            img = _horizontally(img, stretch_factor_h)
            img = _vertically(img, stretch_factor_w)
            img = _rotate_image(img, angle)
            
            image = Image.fromarray(img)
            image.save(f"{output_path_file}/{i}.png")
            
# distortion_run(50)
