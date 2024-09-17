# Distorted Image Generator for Neural Network Training

This project generates a dataset of distorted images for use in training neural networks. The source code creates images of letters, numbers, and other characters, applies various distortions, and outputs these distorted images. These augmented datasets can be beneficial for training neural networks, especially in tasks related to optical character recognition (OCR) or handwritten character classification.

## Features

- **Create Default Character Images:** Generates images for a given set of characters using specified fonts.
- **Apply Distortions:** Applies various distortions (rotation, stretching, offsetting) to the generated images to create a diverse dataset.
- **Supports Multiple Fonts:** Uses different fonts to generate images, enhancing the variability of the training data.
- **Customizable Output:** Allows you to define the list of characters, the number of distorted images to create for each character, and the font size.
- **Organized Output:** Outputs the generated images in a structured directory format, separating uppercase, lowercase, and other characters.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/lxrs312/image_generation.git
    ```
2. Navigate to the project directory:
    ```bash
    cd image_generation
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Generating the Dataset

1. Place your fonts in the `fonts` directory. The program will use these fonts to generate the character images.
2. Adjust the `LETTER_LIST` in `main.py` to include the characters you want to generate images for.
3. Adjust the `SIMULATION_RUNS` in `main.py` to the number of images you want for each character.
4. Run the script:
    ```bash
    python main.py
    ```
5. The output will be generated in the `output_distortions` directory. This directory will contain subdirectories for each font and further subdirectories for uppercase, lowercase, and other characters.

### Example

If the `LETTER_LIST` is set to `"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"`, and you have a font called `Arial.ttf` in the `fonts` directory, running `main.py` will generate distorted images for each of these characters in the specified font.

### Directory Structure

The output directory structure is organized as follows:
```
image_generation/ 
├── create_default_images.py  
├── distort_images.py 
├── exceptions.py
├── main.py
├── tests/
│ └── test_distort_images.py 
│ └── some_test_images.png
├── fonts/
│ └── <font-files> # Font files used to create character images 
├── output_distortions/ # Output directory for distorted images
│ └── your_font
│ │ └── uppercase
│ │ └── lowercase
│ │ └── other
│ └── your_second_font
│ │ └── uppercase
│ │ └── lowercase
│ │ └── other
├── .gitignore 
├── requirements.txt
└── README.md
└── .github/worksflows

```

## Code Structure

### `main.py`

- **`run()`**: Main function that orchestrates the creation of images and application of distortions.
- **`del_output()`**: Clears the output directories if they already exist.

### `create_default_images.py`

- **`create_letter_images()`**: Creates default images for the specified characters using a given font.

### `distort_images.py`

- **`distortion_run()`**: Applies various distortions (rotation, horizontal stretching, vertical stretching, offsetting) to the images.
- **Private Functions**: Helper functions to apply individual distortions:
  - **`_rotate_image()`**: Rotates an image by a specified angle.
  - **`_horizontally()`**: Stretches an image horizontally.
  - **`_vertically()`**: Stretches an image vertically.
  - **`_offset_image()`**: Offsets an image by specified x and y values.

## Running Tests

This project includes unit tests for the functions in `distort_images.py`. To run the tests, use the following command:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### Contributing

If you'd like to contribute to the project, please submit a pull request or open an issue to discuss changes.
