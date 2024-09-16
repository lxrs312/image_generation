import os
from PIL import Image, ImageDraw, ImageFont

def create_letter_images(letter_list: str, font_path: str, output_path: str, image_size: tuple=(32, 32)) -> None:
    
    try:
        font = ImageFont.truetype(font_path, 32)
    except IOError:
        print(f"Could not load font at {font_path}")
        return None
    
    if not os.path.isdir("output"):
        os.mkdir("output")
    
    for letter in letter_list:
        
        # blank image, black bg
        image = Image.new('RGB', image_size, 'black')
        
        draw = ImageDraw.Draw(image)
        bbox = draw.textbbox((0, 0), letter, font=font)
        text_width = bbox[2] - bbox[0]
        
        # calc x,y for drawing the letter/digit
        position = ((image_size[0]-text_width) // 2, 0)
        draw.text(position, letter, font=font, align="left", fill="white")
        
        image.save(f"output/{letter}.png")