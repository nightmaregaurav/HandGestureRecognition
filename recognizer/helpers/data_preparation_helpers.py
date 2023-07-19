import os

from numpy import ndarray
from mediapipe import Image
from mediapipe import ImageFormat


def get_image_from_path(image_path: str) -> Image:
    if not image_path:
        raise ValueError("Image path cannot be empty")
    if not isinstance(image_path, str):
        raise ValueError("Image path must be a string")
    if not os.path.exists(image_path):
        raise ValueError("Image does not exist")

    return Image().create_from_file(file_name=image_path)


def get_image_from_numpy_array(image_array: ndarray) -> Image:
    if not image_array:
        raise ValueError("Image array cannot be empty")
    if not isinstance(image_array, ndarray):
        raise ValueError("Image array must be a numpy array")

    return Image(image_format=ImageFormat.SRGB, data=image_array)


def get_image_from_open_cv_numpy_frame(image_array: ndarray) -> Image:
    return get_image_from_numpy_array(image_array=image_array)
