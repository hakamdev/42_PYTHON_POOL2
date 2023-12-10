# from numpy import zeros, ndarray, sum
import numpy as np
# import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """This function inverts an image.
Args:
    array (ndarray): The image to invert.
    """
    inverted_image = 255 - array
    # plt.imshow(inverted_image)
    # plt.show()
    return inverted_image


def ft_red(array) -> np.ndarray:
    """This function applies a red filter to an image.
Args:
    array (ndarray): The image to apply the red filter.
    """
    red_image = array * [1, 0, 0]
    # plt.imshow(red_image)
    # plt.show()
    return red_image


def ft_green(array) -> np.ndarray:
    """This function applies a green filter to an image.
Args:
    array (ndarray): The image to apply the green filter.
    """
    green_image = np.zeros(array.shape, dtype=int)
    green_image[:, :, 0] = array[:, :, 0] - array[:, :, 0]
    green_image[:, :, 1] = array[:, :, 1]
    green_image[:, :, 2] = array[:, :, 2] - array[:, :, 2]
    return green_image


def ft_blue(array) -> np.ndarray:
    """This function applies a blue filter to an image.
Args:
    array (ndarray): The image to apply the blue filter.
    """
    blue_image = np.zeros(array.shape, dtype=int)
    blue_image[:, :, 0] = 0
    blue_image[:, :, 1] = 0
    blue_image[:, :, 2] = array[:, :, 2]
    # plt.imshow(red_image)
    # plt.show()
    return blue_image


def ft_grey(array) -> np.ndarray:
    """This function applies a greyscale filter to an image.
Args:
    array (ndarray): The image to apply the greyscale filter.
    """
    gray_image = np.zeros(array.shape, dtype=int)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            gray_image[i][j] = np.sum(array[i][j]) / 3
    # plt.imshow(gray_image)
    # plt.show()
    return gray_image
