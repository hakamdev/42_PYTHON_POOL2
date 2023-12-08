from PIL import Image
from numpy import asarray
from numpy import ndarray


def ft_load(path: str) -> ndarray:
    """This function loads an image into a numpy array.
    Args:
        path (str): The path to the image."""
    img = Image.open(path)
    img_arr = asarray(img)
    print(f"The shape of image is: {img_arr.shape}")
    return img_arr
