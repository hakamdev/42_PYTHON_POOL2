from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    image = ft_load("animal.jpeg")
    print(image)

    # slice the image
    w = image.shape[0] // 2
    h = image.shape[1] // 2
    w_offset = w // 2
    h_offset = h // 2
    sliced_image = image[w_offset: w_offset + w, h_offset: h_offset + h]

    # apply grayscale filter
    grayscale_image = sliced_image.copy()
    for i in range(sliced_image.shape[0]):
        for j in range(sliced_image.shape[1]):
            grayscale_image[i][j] = sum(sliced_image[i][j]) / 3

    # display the image
    print(f"New shape after slicing: {grayscale_image.shape}")
    print(grayscale_image)
    plt.imshow(grayscale_image)
    plt.show()


if __name__ == "__main__":
    main()
