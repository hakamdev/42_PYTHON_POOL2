from PIL import Image
from numpy import asarray
from numpy import ndarray


def ft_load(path: str) -> ndarray:
    """This function loads an image into a numpy array.
    Args:
        path (str): The path to the image."""
    try:
        if (type(path) is not str):
            print("AssertionError: path is not a string")
            return None
        if (len(path) == 0):
            print("AssertionError: path is empty")
            return None
        path_segments = path.lower().split(".")
        if (len(path_segments) == 1):
            print("AssertionError: path has no extension")
            return None
        if (path_segments[-1] != "jpeg" and path_segments[-1] != "jpg"):
            print("AssertionError: only jpeg and jpg images are supported")
            return None
        img = Image.open(path)
        img_arr = asarray(img)
        print(f"The shape of image is: {img_arr.shape}")
        print(img_arr)
        return img_arr
    except FileNotFoundError:
        print("AssertionError: file not found")
    except Exception:
        print("AssertionError: image file not supported")
    return None
