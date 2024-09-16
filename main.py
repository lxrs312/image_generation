import os

from create_default_images import create_letter_images
from distort_images import distortion_run

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
OUTPUT_PATH_LETTERS = "output"
OUTPUT_PATH_DISTORTION_LETTERS = "output_distortions"

path = os.path.join(DIR_PATH, OUTPUT_PATH_LETTERS)
print(path)

# Example usage:
font_path = "fonts/BAHNSCHRIFT.TTF"  # Replace with the path to your font file
wanted_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
create_letter_images(wanted_characters, font_path)