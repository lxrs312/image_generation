import cv2
import numpy as np
from PIL import Image
import os
import logging

logger = logging.getLogger(__name__)

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
    # dimensions
    (h, w) = im.shape[:2]

    # blank image with the same dimensions
    blank_image = np.zeros((h, w, 3), dtype=np.uint8)

    # calc new dimensions considering the offset
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

    # calculate the corresponding source region in the original image
    src_y_start = max(-y_offset, 0)
    src_y_end = min(h - y_offset, h)
    src_x_start = max(-x_offset, 0)
    src_x_end = min(w - x_offset, w)

    # place original image onto the blank image with the offset
    blank_image[y_start:y_end, x_start:x_end] = im[src_y_start:src_y_end, src_x_start:src_x_end]

    return blank_image

def _get_case_subdir(letter):
    if letter.isupper():
        return "uppercase"
    elif letter.islower():
        return "lowercase"
    return "others"

def distortion_run(iterations: int, images_dict: dict, output_path: str) -> None:
    """Runs the distortion. This stretches, rotates, and offsets the images.

    Args:
        iterations (int): Number of images generated for each character
        images_dict (dict): Dictionary of images for each character
        output_path (str): Output path for distorted images
    """
    
    for letter, img in images_dict.items():
        logger.info(f"Creating Image for {letter}")
        
        case_subdir = _get_case_subdir(letter)

        # creating a case-specific subdirectory
        case_output_path = os.path.join(output_path, case_subdir)
        os.makedirs(case_output_path, exist_ok=True)

        # create a directory for each letter inside the case-specific subdirectory
        output_path_file = os.path.join(case_output_path, letter)
        os.makedirs(output_path_file, exist_ok=True)

        for i in range(iterations):
            try:
                # distortion-factors
                # maybe put those in some function and give the user the 
                # ability to input a "distortion"-factor.
                stretch_factor_h = np.random.randint(0, 15)
                stretch_factor_w = np.random.randint(0, 15)
                offset_x = np.random.randint(-5, 5)
                offset_y = np.random.randint(-3, 3)
                angle = np.random.randint(-30, 30)

                # copying just to be safe
                img_copy = img.copy() 
                
                # applying distortions
                img_copy = _offset_image(img_copy, offset_x, offset_y)
                img_copy = _horizontally(img_copy, stretch_factor_h)
                img_copy = _vertically(img_copy, stretch_factor_w)
                img_copy = _rotate_image(img_copy, angle)

                # saving it
                image = Image.fromarray(img_copy)
                image.save(f"{output_path_file}/{i}.png")
            except Exception as e:
                logger.error(f"Error distorting image {i} for letter '{letter}': {e}")


image = cv2.imread('tests/test_image.png')
img_offset = _offset_image(image, 10, -10)
img_offset = Image.fromarray(img_offset)
img_horizontally = _horizontally(image, 8)
img_horizontally = Image.fromarray(img_horizontally)
img_vertically = _vertically(image, 8)
img_vertically = Image.fromarray(img_vertically)
img_rotate = _rotate_image(image, 30)
img_rotate = Image.fromarray(img_rotate)

img_offset.save("img_offset.png")
img_horizontally.save("img_horizontally.png")
img_vertically.save("img_vertically.png")
img_rotate.save("img_rotate.png")