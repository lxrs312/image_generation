import os
import shutil
import logging

from create_default_images import create_letter_images
from distort_images import distortion_run
from exceptions import NoFontFoundError

OUTPUT_PATH_LETTERS = "output"
OUTPUT_PATH_DISTORTION_LETTERS = "output_distortions"
FONTS_PATH = "fonts"
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

CLEAR_OUTPUT = True

def del_output():

    try:
        shutil.rmtree(os.path.join(DIR_PATH, OUTPUT_PATH_LETTERS))
        shutil.rmtree(os.path.join(DIR_PATH, OUTPUT_PATH_DISTORTION_LETTERS))
    except PermissionError:
        print("yo")
        pass

def run():
    
    if not os.path.isdir(FONTS_PATH):
        os.mkdir(FONTS_PATH)
    
    fonts = os.listdir(FONTS_PATH)

    # if not fonts:
    #     raise NoFontFoundError
    
    if CLEAR_OUTPUT:
        del_output()
        
    for font in fonts:
        pass
    


# # Example usage:
# font_path = "fonts/BAHNSCHRIFT.TTF"  # Replace with the path to your font file
# wanted_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
# create_letter_images(wanted_characters, font_path)

if __name__ == "__main__":
    run()