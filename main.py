import os
import shutil
import logging

from create_default_images import create_letter_images
from distort_images import distortion_run
from exceptions import NoFontFoundError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
OUTPUT_PATH_DISTORTION_LETTERS = os.path.join(DIR_PATH, "output_distortions")
FONTS_PATH = os.path.join(DIR_PATH, "fonts")

LETTER_LIST = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

CLEAR_OUTPUT = True

def del_output():
    # Deleting existing output
    try:
        if os.path.isdir(OUTPUT_PATH_DISTORTION_LETTERS):
            shutil.rmtree(OUTPUT_PATH_DISTORTION_LETTERS)
    except PermissionError as e:
        logger.error(f"Error deleting output directories: {e}")

def run():
    logger.info("Starting image generation.")

    # Create fonts directory if it is not there
    if not os.path.isdir(FONTS_PATH):
        os.mkdir(FONTS_PATH)
    
    fonts = os.listdir(FONTS_PATH)
    if not fonts:
        raise NoFontFoundError

    # Clear the output directories
    if CLEAR_OUTPUT:
        logger.info("Clearing already existing files.")
        del_output()
    
    # Create main output directory
    os.makedirs(OUTPUT_PATH_DISTORTION_LETTERS, exist_ok=True)

    for font in fonts:
        try:
            # Create font-specific output directories
            font_name = font.split(".")[0]
            font_specific_output_path_distorted = os.path.join(OUTPUT_PATH_DISTORTION_LETTERS, font_name)
            os.makedirs(font_specific_output_path_distorted, exist_ok=True)
            
            logger.info(f"Creating images for {font_name}.")

            # Create default letter images
            default_letter_dict = create_letter_images(LETTER_LIST, os.path.join(FONTS_PATH, font))
            if not default_letter_dict:
                logger.warning(f"Skipping font {font} due to errors in image creation.")
                continue

            # Create distorted images
            distortion_run(10, default_letter_dict, font_specific_output_path_distorted)

        except Exception as e:
            logger.error(f"Error processing font {font}: {e}")

if __name__ == "__main__":
    run()
