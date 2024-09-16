import unittest
import numpy as np
import cv2
from distort_images import (
    _rotate_image,
    _horizontally,
    _vertically,
    _offset_image,
    distortion_run,
)
import os
import shutil

class TestDistortImages(unittest.TestCase):

    def setUp(self):
        # Create a dummy image (32x32 pixels, black background)
        self.image = cv2.imread('tests/test_image.png')
        print(self.image)
        self.output_dir = "test_output"

    def tearDown(self):
        # Clean up the output directory
        if os.path.isdir(self.output_dir):
            shutil.rmtree(self.output_dir)

    def test_rotate_image(self):
        rotated_image = _rotate_image(self.image, 45)
        self.assertEqual(rotated_image.shape, self.image.shape)
        self.assertFalse(np.array_equal(rotated_image, self.image))  # Should be different

    def test_horizontally(self):
        stretched_image = _horizontally(self.image, 5)
        self.assertEqual(stretched_image.shape, self.image.shape)
        self.assertFalse(np.array_equal(stretched_image, self.image))  # Should be different

    def test_vertically(self):
        stretched_image = _vertically(self.image, 5)
        self.assertEqual(stretched_image.shape, self.image.shape)
        self.assertFalse(np.array_equal(stretched_image, self.image))  # Should be different

    def test_offset_image(self):
        offset_image = _offset_image(self.image, 5, 5)
        self.assertEqual(offset_image.shape, self.image.shape)
        self.assertFalse(np.array_equal(offset_image, self.image))  # Should be different

    def test_distortion_run(self):
        images_dict = {'A': self.image}
        distortion_run(5, images_dict, self.output_dir)
        # Check if files are created
        uppercase_dir = os.path.join(self.output_dir, 'uppercase', 'A')
        self.assertTrue(os.path.isdir(uppercase_dir))
        self.assertEqual(len(os.listdir(uppercase_dir)), 5)

if __name__ == '__main__':
    unittest.main()
