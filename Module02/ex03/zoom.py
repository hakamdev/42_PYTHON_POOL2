from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    image = ft_load("animal.jpeg")
    if (image is None):
        return
    print(image)

    # slice the image
    half_w = image.shape[0] // 2
    half_h = image.shape[1] // 2
    w_offset = half_w // 2
    h_offset = half_h // 2
    shortest_side = min(half_w, half_h)
    sliced_image = image[w_offset: w_offset + shortest_side,
                         h_offset: h_offset + shortest_side]

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
