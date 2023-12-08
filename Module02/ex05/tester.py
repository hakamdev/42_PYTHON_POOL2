from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


array = ft_load("landscape.jpeg")
inverted_img = ft_invert(array)
red_img = ft_red(array)
green_img = ft_green(array)
blue_img = ft_blue(array)
gray_img = ft_grey(array)
print(ft_invert.__doc__)

# displaying all images
images = [array, inverted_img, red_img, green_img, blue_img, gray_img]
fig = plt.figure(figsize=(8, 8))
columns = 2
rows = 3
for i in range(columns * rows):
    fig.add_subplot(rows, columns, i + 1)
    plt.imshow(images[i])
plt.show()
