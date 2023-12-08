from numpy import zeros, ndarray
# import matplotlib.pyplot as plt


def ft_invert(array) -> ndarray:
    """This function inverts an image.
    Args:
        array (ndarray): The image to invert.
    """
    inverted_image = zeros(array.shape, dtype=int)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            inverted_image[i][j] = 255 - array[i][j]
    # plt.imshow(inverted_image)
    # plt.show()
    return inverted_image


def ft_red(array) -> ndarray:
    """This function applies a red filter to an image.
    Args:
        array (ndarray): The image to apply the red filter.
    """
    red_image = zeros(array.shape, dtype=int)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            red_image[i][j] = [array[i][j][0], 0, 0]
    # plt.imshow(red_image)
    # plt.show()
    return red_image


def ft_green(array) -> ndarray:
    """This function applies a green filter to an image.
    Args:
        array (ndarray): The image to apply the green filter.
    """
    green_image = zeros(array.shape, dtype=int)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            green_image[i][j] = [0, array[i][j][1], 0]
    # plt.imshow(green_image)
    # plt.show()
    return green_image


def ft_blue(array) -> ndarray:
    """This function applies a blue filter to an image.
    Args:
        array (ndarray): The image to apply the blue filter.
    """
    red_image = zeros(array.shape, dtype=int)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            red_image[i][j] = [0, 0, array[i][j][2]]
    # plt.imshow(red_image)
    # plt.show()
    return red_image


def ft_grey(array) -> ndarray:
    """This function applies a greyscale filter to an image.
    Args:
        array (ndarray): The image to apply the greyscale filter.
    """
    gray_image = zeros(array.shape, dtype=int)
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            gray_image[i][j] = sum(array[i][j]) / 3
    # plt.imshow(gray_image)
    # plt.show()
    return gray_image
