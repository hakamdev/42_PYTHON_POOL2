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
titles = ["Original Image", "Inverted Image", "Red Image", "Green Image",
          "Blue Image", "Gray Image"]
fig = plt.figure(figsize=(10, 10))
columns = 2
rows = 3
for i in range(columns * rows):
    ax = fig.add_subplot(rows, columns, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i])
fig.tight_layout(pad=5.0)
plt.show()
