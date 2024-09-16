import numpy as np
from PIL import Image, ImageDraw, ImageFont
import logging

logger = logging.getLogger(__name__)

def create_letter_images(letter_str: str, font_path: str, image_size: tuple = (32, 32), font_size: int = 26) -> dict:
    """Creates images of the given characters using the font specified in the font_path.

    Args:
        letter_str (str): String consisting of all letters that an image should be generated for
        font_path (str): Path to the font
        image_size (tuple, optional): Image size as an integer tuple. Defaults to (32, 32).
        font_size (int, optional): Font size. Defaults to 26.

    Returns:
        dict: Dictionary containing the characters and their numpy representation
    """
    images_dict = {}
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        logger.error(f"Could not load font at {font_path}")
        return {}

    for letter in letter_str:
        # blank image, black bg
        image = Image.new('RGB', image_size, 'black')
        
        draw = ImageDraw.Draw(image)
        bbox = draw.textbbox((0, 0), letter, font=font)
        text_width = bbox[2] - bbox[0]
        
        # calc x, y for drawing the letter/digit, x->mid, y always 0
        position = ((image_size[0] - text_width) // 2, 0)
        draw.text(position, letter, font=font, align="left", fill="white")
        
        # convert to npy
        image_np = np.array(image)
        
        # store it in dict
        images_dict[letter] = image_np
        
    
    return images_dict
